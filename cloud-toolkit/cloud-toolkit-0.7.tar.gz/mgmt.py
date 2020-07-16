from texttable import Texttable, get_color_string, bcolors
import boto3
import argparse
import sys,json
import configparser
from remote import IoTOperation
import time, datetime
import curses

AllowedActions = ['subscribe']

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', action='store', dest='target', default='aws',
                    help='connection target')

stdscr = None
client = None

def get_var(input_dict, accessor_string):
    """Gets data from a dictionary using a dotted accessor-string"""
    current_data = {}
    if 'desired' in input_dict:
        current_data['desired'] = input_dict['desired']
    if 'reported' in input_dict:
        current_data['reported'] = input_dict['reported']
    if accessor_string == '':
        return current_data
    for chunk in accessor_string.split('.'):
        if chunk == '':
            return current_data
        if chunk not in current_data:
            return current_data
        current_data = current_data[chunk]
    return current_data

def table_line(stdscr, y, w):
    stdscr.addstr(y,   5, '+'+'-'*int(w*0.6-2)+'+'+'-'*int(w*0.4-2)) 

def twin_pad(stdscr, shadow, twin_query):
    height, width = stdscr.getmaxyx()
    prop = get_var(shadow, twin_query)
    props = []

    prop_content = json.dumps(prop, sort_keys=True , indent=4)
    props = prop_content.splitlines()

    padhlines = (height-5-5-2)
    padwcols = int(width/2-2)
    stdscr.addstr(5-1, padwcols+3, "Device Twin Content", curses.color_pair(2)|curses.A_BOLD)

    mypads = stdscr.subpad(padhlines, padwcols, 5, int(width/2))
    mypads.scrollok(1)
    mypads.idlok(1)
    mypads.border(0) # ... border
    prop_x = 1
    for p in props:
        if padhlines > prop_x:
            mypads.addstr(prop_x, 2, p)
            prop_x+=1
    mypads.border(0) # ... border
    mypads.refresh()
    mypads.touchwin()


class sub_obj:
    def __init__(self, topic, win=None, client=None):
        self.win = win
        self.client = client
        self.topic = topic
        self.message = ''
        self.recv_topic = ''
        self.last_time = ''
    def message_callback(self, topic, message):
        self.message = message.decode('utf-8')
        self.recv_topic = topic.decode('utf-8')
        self.last_time = str(datetime.datetime.now())
        self.draw()

    def sub(self, topic):
        if len(self.topic) > 0:
            self.client.unsubscribe_messages(self.topic)
        self.client.subscribe_messages(topic, callback=self.message_callback)
        self.topic = topic
    def draw(self):
        height, width = self.win.getmaxyx()
        padhlines = (height-18-2-2-5)
        padwcols = int(width/2-5-5-2)

        #self.win.addstr(18+1, 5+1, 'Start subscribe topic: '+self.topic, curses.color_pair(2)|curses.A_BOLD)
        mypads = self.win.subpad(padhlines, padwcols, 18+2, 5)
        mypads.clear()
        mypads.scrollok(1)
        mypads.idlok(1)
        mypads.border(0) # ... border
        if len(self.message) > 0:
            lines = self.message.splitlines()
            mypads.addstr(1, 2, 'Received a new message from topic: '+self.recv_topic+','+self.last_time)
            prop_x = 2
            for p in lines:
                mypads.addstr(prop_x, 2, p)
                prop_x+=1
        mypads.border(0) # ... border
        mypads.refresh()
        mypads.touchwin()

class cmd_helper:
    def __init__(self, win=None, client=None):
        self.win = win
        self.client = client
        self.state = 'no'
        self.select = ''
        self.input_state = 0
        self.data = ''
        self.result = ''
        self.content0 = '''
Suppport commands:
 (1) thingspro-api-v1
 (2) system-reboot
 (3) thingspro-applications-control
 (4) thingspro-software-upgrade
 (5) open-secure-tunnel
'''
        self.content1 = '''
Select : {}
'''
        self.content2 = '''
Input  : {}
'''
        self.content3 = '''
Result : {}
'''

    def input(self, data):
        if self.state == 'wait':
            self.select = data
        else:
            self.data = data

    def do(self, dev_select):
        if self.select == '1':
            state, resp = client.command(dev_select['name'], "thingspro-api-v1", self.data)
            self.result = '{}, {}'.format(state, resp)
        elif self.select == '2':
            state, resp = client.command(dev_select['name'], "system-reboot", '{}')
            self.result = '{}, {}'.format(state, resp)
        elif self.select == '3':
            state, resp = client.command(dev_select['name'], "thingspro-applications-control", self.data)
            self.result = '{}, {}'.format(state, resp)
        elif self.select == '4':
            state, resp = client.command(dev_select['name'], "thingspro-software-upgrade", self.data)
            self.result = '{}, {}'.format(state, resp)
        elif self.select == '5':
            result = self.client.open_tunnel(dev_select['name'], "SSH", 5555)
            if result != '':
                self.result = '400, tunnel create failed, error:', result
            else:
                self.result = '200, tunnel create success, token file: /data/.aws_tunnel.ini'

    def clear(self):
        self.select = ''
        self.result = ''
        self.data = ''

    def command_wait(self, dev_select):
        k = 0
        cmd_str = ''
        while True:
            k = self.win.getch()
            if k == 10:
                break
            if k == 27:
                return False
            cmd_str += chr(k)
            self.input(cmd_str)
            self.draw(True, dev_select)
        return True

    def command(self, dev_select, next=False):
        '''no -> wait -> input -> submit -> no'''
        while True:
            if next == False:
                return
            elif self.state == 'no':
                self.state = 'wait'
                self.draw(True, dev_select['name'])
                if self.command_wait(dev_select['name']) == False:
                    return
                continue
            elif self.state == 'wait':
                self.state = 'input'
                self.draw(True, dev_select['name'])
                if self.select == '5':
                    continue
                if self.command_wait(dev_select['name']) == False:
                    return
                continue
            elif self.state=='input':
                self.state = 'submit'
                self.do(dev_select)
                self.draw(True, dev_select['name'])
                continue
            elif self.state=='submit':
                self.state = 'no'
                return

    def draw(self, show, device_name):
        content = ''
        if show == False:
            return
        
        height, width = self.win.getmaxyx()
        padhlines = (height-18-2-2-5)
        padwcols = int(width/2-5-5-2)

        self.win.addstr(18+1, 5+1, " "*padwcols)
        self.win.addstr(18+1, 5+1, 'Invoke Command to : '+ device_name, curses.color_pair(2)|curses.A_BOLD)
        mypads = self.win.subpad(padhlines, padwcols, 18+2, 5)
        mypads.clear()
        mypads.scrollok(1)
        mypads.idlok(1)
        mypads.border(0) # ... border

        # selection list
        prop_x = 1
        lines = self.content0.splitlines()
        for p in lines:
            if prop_x >= padhlines:
                    break
            mypads.addstr(prop_x, 2, p)
            prop_x+=1

        # select mode
        content = self.content1.format(self.select)
        lines = content.splitlines()
        if self.state == 'wait':
            for p in lines:
                if prop_x >= padhlines:
                    break
                mypads.addstr(prop_x, 2, p, curses.color_pair(6)|curses.A_BOLD)
                prop_x+=1
        else:
            for p in lines:
                if prop_x >= padhlines:
                    break
                mypads.addstr(prop_x, 2, p)
                prop_x+=1

        # input arg
        content = self.content2.format(self.data)
        lines = content.splitlines()
        if self.state == 'input':
            for p in lines:
                if prop_x >= padhlines:
                    break
                mypads.addstr(prop_x, 2, p, curses.color_pair(6)|curses.A_BOLD)
                prop_x+=1
        else:
            for p in lines:
                if prop_x >= padhlines:
                    break
                mypads.addstr(prop_x, 2, p)
                prop_x+=1

        content = self.content3.format(self.result)
        lines = content.splitlines()
        if self.state == 'submit':
            for p in lines:
                if prop_x >= padhlines:
                    break
                mypads.addstr(prop_x, 2, p)
                prop_x+=1
        else:
            for p in lines:
                if prop_x >= padhlines:
                    break
                mypads.addstr(prop_x, 2, p)
                prop_x+=1

        mypads.border(0) # ... border
        mypads.refresh()
        mypads.touchwin()

class msg_helper:
    def __init__(self, topic, win=None, client=None):
        self.win = win
        self.client = client
        self.topic = topic
        self.message = ''
        self.last_time = ''
    def message_callback(self, client, userdata, message):
        self.message = message.payload.decode('utf-8')
        self.last_time = str(datetime.datetime.now())
        self.draw(False, '')

    def sub(self, topic):
        if len(self.topic) > 0:
            self.client.unsubscribe_messages(self.topic)
        self.client.subscribe_messages(topic, callback=self.message_callback)
        self.topic = topic

    def command_wait(self):
        k = 0
        topic = ''
        self.draw(True, topic)
        while True:
            k = self.win.getch()
            if k == 10:
                break
            if k == 27:
                return ''
            topic += chr(k)
            self.draw(True, topic)
        return topic

    def draw(self, wait, temp):
        height, width = self.win.getmaxyx()
        padhlines = (height-18-2-2-5)
        padwcols = int(width/2-5-5-2)

        if wait == True:
            self.win.addstr(18+1, 5+1, 'Input subscribe topic(press Enter to continue): '+temp, curses.color_pair(2)|curses.A_BOLD)
        else:
            self.win.addstr(18+1, 5+1, 'Start subscribe topic: '+self.topic, curses.color_pair(2)|curses.A_BOLD)

        mypads = self.win.subpad(padhlines, padwcols, 18+2, 5)
        mypads.clear()
        mypads.scrollok(1)
        mypads.idlok(1)
        mypads.border(0) # ... border
        if len(self.message) > 0:
            lines = self.message.splitlines()
            mypads.addstr(1, 2, 'Received a new message from topic: '+self.topic+','+self.last_time)
            prop_x = 2
            for p in lines:
                mypads.addstr(prop_x, 2, p)
                prop_x+=1
        mypads.border(0) # ... border
        mypads.refresh()
        mypads.touchwin()

def page(stdscr):
    stdscr = stdscr
    k = 0
    cursor_x = 0
    cursor_y = 0
    device_start_idx = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)

    twin_mode = False
    twin_str = ''
    msg_mode = False
    cmd_mode = False
    cmd_str = ''
    dev_select = {}

    sub_win = msg_helper('', win=stdscr, client=client)
    cmd_win = cmd_helper(win=stdscr, client=client)

    devices = client.search_devices()
    refresh = False
    dev_update = False

    # Loop where k is the last character pressed
    while (k != 27):
        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 2
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 2
        elif k == curses.KEY_F5:
            twin_mode = True
            msg_mode = False
            cmd_mode = False
            twin_str = ''
        elif k == curses.KEY_F6:
            msg_mode = True
            cmd_mode = False
            twin_mode = False
            topic = sub_win.command_wait()
            if topic == '':
                msg_mode = False
            else:
                sub_win.sub(topic)
        elif k == curses.KEY_F7:
            cmd_mode = True
            msg_mode = False
            twin_mode = False
            cmd_win.clear()
            cmd_win.command(dev_select, True)
        elif k == curses.KEY_F8:
            devices = client.search_devices()
        elif k == curses.KEY_F9:
            dev_update = True
            dev_select = client.search_device(dev_select['name'])[0]
        elif twin_mode:
            twin_str += chr(k)

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Rendering some text
        whstr = "Width: {}, Height: {}".format(width, height)
        stdscr.addstr(0, 0, whstr, curses.color_pair(1))

        start_y = 5
        start_x = 5
        col_width = 50
        left_win_width = int(width/2-5-5)
        start_x_name = start_x+1
        start_x_state = int(left_win_width*0.6+5)

        # Rendering title
        title = 'Cloud Device Management Interface'[:width-1]
        stdscr.addstr(start_y-1, 6, title, curses.color_pair(2)|curses.A_BOLD)
        table_line(stdscr, start_y, left_win_width)
        stdscr.addstr(start_y+1, start_x_name, 'Thing Name')
        stdscr.addstr(start_y+1, start_x_state, 'State')
        table_line(stdscr, start_y+2, left_win_width)
        start_y += 3

        floor = 16
        if cursor_y <= 0:
            cursor_y = start_y
        elif cursor_y < start_y and device_start_idx > 0:
            device_start_idx-=1
            cursor_y = start_y
        elif cursor_y < start_y:
            cursor_y = start_y
        elif cursor_y > floor and int(device_start_idx+1+int((cursor_y-8)/2)) > len(devices):
            cursor_y = floor
        elif cursor_y > floor:
            device_start_idx+=1
            cursor_y = floor
        stdscr.addstr(cursor_y, 1, "=>", curses.color_pair(1))

        # Render status bar
        if dev_update == False:
            dev_select = devices[int(device_start_idx + (cursor_y - 8) / 2)]
        else:
            dev_update = True

        thing_info = "Device Name: {}".format(dev_select['name'])
        if twin_mode:
            thing_info += ", Enter twin query: "+ str(twin_str)
            stdscr.addstr(height-2, 0, thing_info, curses.color_pair(4))
            stdscr.addstr(height-2, len(thing_info), " " * (width - len(thing_info) - 1), curses.color_pair(4))
        elif cmd_mode:
            thing_info += ", Enter command input(Press Enter to subimt)"
            stdscr.addstr(height-2, 0, thing_info, curses.color_pair(4))
            stdscr.addstr(height-2, len(thing_info), " " * (width - len(thing_info) - 1), curses.color_pair(4))

        # twin pad
        shadow = {'desired':dev_select['desired'], 'reported':dev_select['reported']}
        twin_pad(stdscr, shadow, twin_str)

        # msg pad
        sub_win.draw(False, '')

        # msg pad
        cmd_win.draw(cmd_mode, dev_select['name'])

        # Render status bar
        statusbarstr = "Press ESC to exit | F5 to twin | F6 to message | F7 to command | F8 to refresh devs | F9 to refresh dev | Pos: {}".format(cursor_y)
        stdscr.addstr(height-1, 0, statusbarstr, curses.color_pair(4))
        stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1), curses.color_pair(4))

        # Rendering device list
        for m in range(5):
            if device_start_idx + m >= len(devices):
                stdscr.addstr(start_y + m*2, start_x_name, ' '*col_width, curses.color_pair(3))
                stdscr.addstr(start_y + m*2, start_x_state, ' '*10, curses.color_pair(5))
                table_line(stdscr, start_y + m*2+1, left_win_width)
                continue

            device = devices[device_start_idx + m]
            name = device['name'][:width-1]
            stdscr.addstr(start_y + m*2, start_x_name, name, curses.color_pair(3))
            if device['connected']:
                stdscr.addstr(start_y + m*2, start_x_state, 'connected', curses.color_pair(5))
            else:
                stdscr.addstr(start_y + m*2, start_x_state, 'disconnect', curses.color_pair(6))
            table_line(stdscr, start_y + m*2+1, left_win_width)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

#----------------------------------------------------------------
args = parser.parse_args()

# read config
config = configparser.ConfigParser()
config.read('./setting.ini')

# init cloud iot client
client = IoTOperation(args.target, config[args.target])

curses.wrapper(page)
