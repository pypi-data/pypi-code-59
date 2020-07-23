#!/usr/bin/env python3
#  Copyright (c) 2019 MindAffect B.V. 
#  Author: Jason Farquhar <jason@mindaffect.nl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from mindaffectBCI.noisetag import Noisetag, sumstats
from psychopy import prefs
prefs.general['winType']='pyglet'
from psychopy import visual, core, event, logging, gui

# dictionary mapping from stimulus-state to colors'
# N.B. pyschopy rgb color space is -1:+1
state2color={0:( -.4, -.4, -.4), # off=grey
             1:(   1,   1,   1),    # on=white
             2:(  -1,   1,  -1),    # cue=green
             3:(  -1,  -1,   1)}    # feedback=blue
def draw(dt=0):
    '''draw the display with colors from noisetag'''
    global nt, tsClock, window
    # send info on the *previous* stimulus state, with the recorded vsync time (if available)
    fliptime = tsClock.psychoPy2utopiaTimeStamp(window.lastfliptime)
    curtime = tsClock.getTimeStamp()
    #print("dt = {} - {} = {} ".format(curtime,fliptime,curtime-fliptime))
    nt.sendStimulusState(timestamp=fliptime)
    # update and get the new stimulus state to display
    try : 
        nt.updateStimulusState()
        stimulus_state,target_state,objIDs,sendEvents=nt.getStimulusState()
    except StopIteration :
        exit()
        return

    # draw the display with the instructed colors
    if stimulus_state :
        # N.B. in norm units screen is -1,-1 -> +1,+1
        w=.4; h=.4
        rect = visual.Rect(win=window, units='norm', width=w, height=h, opacity=1.0, fillColorSpace='rgb')
        # N.B. Rect position is relative to its center
        # draw square 1
        rect.pos = (-.6,0)
        rect.fillColor= state2color[stimulus_state[0]]
        rect.draw()
        # draw square 2
        rect.pos = (.6,0)
        rect.fillColor= state2color[stimulus_state[1]]
        rect.draw()

        if target_state is not None and target_state >= 0 :
            # opto sensor at top-left
            rect.pos=(-1,1)
            rect.fillColor=state2color[1 if target_state==1 else 0]
            rect.draw()

    # some textual logging of what's happening
    if target_state is not None and target_state>=0:
        print("*" if target_state>0 else '.',end='',flush=True)
    else:
        print('.',end='',flush=True)


class PsychoPyTimeStampClock:
    ''' class wrapping PsychoPy frame clock to work with utopia '''
    def getTimeStamp(self):
        return logging.defaultClock.getTime()*1000.0

    def psychoPy2utopiaTimeStamp(self, ts):
        return ts*1000.0
# global clock based on psychopy
tsClock = PsychoPyTimeStampClock()

# define a trival selection handler
def selectionHandler(objID):
    print("Selected: %d"%(objID))    

# Initialize the drawing window
# N.B. before nt so can use this window to query IP if needed
# make a default window with wait blanking
window = visual.Window([1024,768], winType='pyglet', waitBlanking=True, 
                       monitor='testMonitor', units='norm', 
                       fullscr=True)
# log frame timing information
window.recordFrameIntervals = True
logging.console.setLevel(logging.WARNING)
# Setup the flip-time recording for this window
window.lastfliptime=tsClock.getTimeStamp()

host=None
# Initialize the noise-tagging connection
nt = Noisetag()
visual.TextStim(window,text="Trying to auto-connect to mindaffectBCI\nPlease wait").draw()
window.flip()
nt.connect(host=host, timeout_ms=5000, queryifhostnotfound=False)
if not nt.isConnected():
    visual.TextStim(window,text="Host not found, enter in dialog box:").draw()
    window.flip()
    textBox = gui.Dlg(title='Host not found, enter the host IP')
    textBox.addField('Host IP: ', host)
    textBox.show()
    if textBox.OK:
        host= textBox.data[0]
    else:
        host= None
    if host is not None:
        nt.connect(host=host, timeout_ms=5000, queryifhostnotfound=False)

nt.addSelectionHandler(selectionHandler)
# tell the noisetag framework to run a full : calibrate->prediction sequence
nt.setnumActiveObjIDs(2)
nt.startExpt(nCal=10, nPred=10, duration=4, cuedprediction=True)

# override default time-stamp clock with Psychopy's so all messages
# use the same time-stamp system
try:
    nt.setTimeStampClock(tsClock)
except:
    print("setting time-stamp clock not supported?")
    
# run application
while True:
    draw()
    # record the flip-time in 'lastfliptime', N.B. re-add *every frame*
    window.timeOnFlip(window,'lastfliptime')
    window.flip()