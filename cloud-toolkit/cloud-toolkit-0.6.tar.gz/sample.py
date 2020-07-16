import argparse
import sys,json
import configparser
from remote import IoTOperation
import time, datetime
import curses

AllowedActions = ['subscribe', 'list', 'command', 'device', 'desired']

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', action='store', dest='target', default='aws',
                    help='connection target')
parser.add_argument('-m', '--mode', action='store', dest='mode', default='subscribe',
                    help='Operation modes: %s'%str(AllowedActions))
parser.add_argument("-T", "--topic", action="store", dest="topic", default="#",
                    help="Targeted topic")
parser.add_argument("-D", "--device", action="store", dest="device", default="mydev",
                    help="control device")
parser.add_argument("-C", "--command", action="store", dest="command_name", default="thingspro-api-v1",
                    help="control command name")
parser.add_argument("-P", "--payload", action="store", dest="command_payload", default="{}",
                    help="control command payload")
parser.add_argument("-S", "--desired_payload", action="store", dest="desired_payload", default="{}",
                    help="desired payload")
parser.add_argument("--pretty", action="store_true", dest="pretty", default=False,
                    help="pretty json output")

args = parser.parse_args()
json_indent = None
if args.pretty:
        json_indent = 4

def message_callback(topic, payload):
        print('Received a new message from topic: '+topic)
        print(payload)
        print('--------------\n\n')

# read config
config = configparser.ConfigParser()
config.read('./setting.ini')

# init cloud iot client
client = IoTOperation(args.target, config[args.target])

if args.mode == 'list':
        devices_shadow = client.search_devices()
        print(json.dumps(devices_shadow, indent=json_indent))
        sys.exit()

if args.mode == 'device':
        device_shadow = client.search_device(args.device)
        if len(device_shadow) <= 0:
                print(args.device+'is not found')
                sys.exit()
        print(json.dumps(device_shadow[0], indent=json_indent))
        sys.exit()

if args.mode == 'desired':
        status_code = client.desired(args.device, args.desired_payload)
        print(status_code)
        sys.exit()

if args.mode == 'command':
        code, resp = client.command(args.device, args.command_name, args.command_payload)
        print('code: ' + str(code))
        print('response: ' + json.dumps(resp, indent=json_indent))
        sys.exit()

if args.mode == 'subscribe':
        client.subscribe_messages(args.topic, callback=message_callback)
        try:
                while True:
                        time.sleep(5)
        except KeyboardInterrupt:
                client.unsubscribe_messages(args.topic)
                sys.exit()