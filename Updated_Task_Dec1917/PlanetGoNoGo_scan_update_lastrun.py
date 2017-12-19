#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04), Tue Dec 19 16:50:08 2017
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'RewardGoNoGo'  # from the Builder filename that created this script
expInfo = {u'mriMode': u'Scan', u'runOrder': u'A', u'hand': u'right', u'session': u'001', u'stimType': u'c', u'participant': u'test', u'colorVersion': u'1crater'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/Katie/Dropbox/Planets/ForGithub/Updated_Task_Dec1917/PlanetGoNoGo_scan_update.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='deg')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
welcomeScreen = visual.TextStim(win=win, ori=0, name='welcomeScreen',
    text=u'Welcome to the planets game!',    font=u'Arial',
    pos=[0, 0], height=2, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
polygon = visual.Rect(win=win, name='polygon',
    width=[2, 2][0], height=[2, 2][1],
    ori=0, pos=[-15, 12],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)

# Initialize components for Routine "Directions"
DirectionsClock = core.Clock()
direction1 = visual.TextStim(win=win, ori=0, name='direction1',
    text='You will be traveling through different galaxies. You can win or lose different amounts of money in each galaxy.  \n \nIf you see a circle with 1 star, that means you can win or lose a low amount. If you do well, you will earn 20 cents, but if you make a mistake, you will lose 10 cents. \n \nIf you see a circle with 2 stars, that means you can win or lose a high amount. You can earn 1 dollar or lose 50 cents. ',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
colorTrialsFile = os.path.join('conditions', 'RewardGoNoGo_Version%s.xlsx' % expInfo['colorVersion'])
logging.exp("Using trial color file: %s" % colorTrialsFile)
runOrderFile = os.path.join('conditions', 'GalaxyValues%s.xlsx' % expInfo['runOrder'])
logging.exp("Using run order file: %s" % runOrderFile)

# Initialize components for Routine "directions2"
directions2Clock = core.Clock()
directionsText2 = visual.TextStim(win=win, ori=0, name='directionsText2',
    text="First you will see a cue to show you the stakes of the block.  \n \nNext you will see planets or asteroids. Only click for planets! If it is a planet, click your pointer finger as quickly as possible, but don't click the asteroids! \n \nAt the end of a block, you will see how much you earned, and then you will get a short break. ",    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
waitForTrigger = visual.TextStim(win=win, ori=0, name='waitForTrigger',
    text='Get Ready!',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "waitForScanner"
waitForScannerClock = core.Clock()
fmriClock = core.Clock()
#trigger = 'usb'
#trigger = 'parallel'
#if trigger == 'parallel':
#    from psychopy.contrib import parallel as winioport
#    #from psychopy import parallel
#elif trigger == 'usb':
#    from psychopy.hardware.emulator import launchScan
    #
    # settings for launchScan:
#    MR_settings = { 
#        'TR': 2.000, # duration (sec) per volume
#        'volumes': 210, # number of whole-brain 3D volumes / frames
#        'sync': 'equal', # character to use as the sync timing event; assumed to come at start of a volume
#        'skip': 0, # number of volumes lacking a sync pulse at start of scan (for T1 stabilization)
#        }

# for GSR sync
#import serial
#class HvdSerial(serial.Serial):
#    def writeUSB(self,dest,val):
#        self.write(chr(dest))
#        self.write(chr(val))

#try:
#    ser = HvdSerial('/dev/tty.usbmodem12341',timeout=1)
    # Zero Out Parallel & BNC
#    ser.writeUSB(0,0)
#    core.wait(.3)
#    ser.writeUSB(1,0)
#    core.wait(.3)
#except serial.SerialException:
#    ser = None
#    logging.warn('No Serial Device Found.')


# Initialize components for Routine "trial_cue"
trial_cueClock = core.Clock()
# set border color
borderColor='black'
valueCondition=None
valueConditions=None

Cue2 = visual.ImageStim(win=win, name='Cue2',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[12.5, 10],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
frame1 = visual.Rect(win=win, name='frame1',
    width=[18, 18][0], height=[18, 18][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-3.0, 
interpolate=True)
frame2 = visual.Rect(win=win, name='frame2',
    width=[19, 19][0], height=[19, 19][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
allISIs=[3.5, 2.5, 3, 2.5, 1.5, 2, 1.5, 2.5]

import copy, random
rotations=[45, 90, 135, 180, 225, 270, 315, 360]

import copy, random
drawCircle = visual.Polygon(win=win, name='drawCircle',
    edges = 90, size=[16.5, 16.5],
    ori=0, pos=[0, 0],
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)
import time
expInfo['expStartTime'] = time.ctime()

BLOCK_DURATION = 10
blockClock = core.Clock()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()

fixation1 = visual.TextStim(win=win, ori=0, name='fixation1',
    text='default text',    font='Arial',
    pos=[0, 0], height=1.5, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)
fixationFrame1 = visual.Rect(win=win, name='fixationFrame1',
    width=[18, 18][0], height=[18, 18][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
fixationFrame2 = visual.Rect(win=win, name='fixationFrame2',
    width=[19, 19][0], height=[19, 19][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-3.0, 
interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()


targetType=None
prepot=None
# set border color
borderColor='black'

# Assumes "first key" or "last key" was chosen for store.
# List conversion (to single key) happens immediately
# when component finishes.
def check_correct(keys,correct):
    if len(keys):  # At least 1 response
        if keys == correct:
            return True
        else:
            return False
    else:  # No response
        if correct == None:
            return True
        else:
            return False

# set outcome values
outcomeNumber='0'
outcomeText='0'



trialFrame = visual.Rect(win=win, name='trialFrame',
    width=[18, 18][0], height=[18, 18][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='white', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-4.0, 
interpolate=True)
trialFrame2 = visual.Rect(win=win, name='trialFrame2',
    width=[19, 19][0], height=[19, 19][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor='black', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-5.0, 
interpolate=True)
Target = visual.ImageStim(win=win, name='Target',
    image='sin', mask=None,
    ori=1.0, pos=[0, 0], size=[15, 15],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=True, flipVert=False,
    texRes=256, interpolate=True, depth=-6.0)


# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitteredISI = visual.TextStim(win=win, ori=0, name='jitteredISI',
    text='+',    font='Arial',
    pos=[0, 0], height=1.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
jitterFrame1 = visual.Rect(win=win, name='jitterFrame1',
    width=[18, 18][0], height=[18, 18][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
jitterFrame2 = visual.Rect(win=win, name='jitterFrame2',
    width=[19, 19][0], height=[19, 19][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)


RT=None
goRT=None


# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
# set reward text color
rewardColor='white'
reward = visual.TextStim(win=win, ori=0, name='reward',
    text='default text',    font='Arial',
    pos=[0, 0], height=2, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0)
rewardFrame1 = visual.Rect(win=win, name='rewardFrame1',
    width=[18, 18][0], height=[18, 18][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
rewardFrame2 = visual.Rect(win=win, name='rewardFrame2',
    width=[19, 19][0], height=[19, 19][1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-3.0, 
interpolate=True)


# Initialize components for Routine "endBlock"
endBlockClock = core.Clock()
breakFixation = visual.TextStim(win=win, ori=0, name='breakFixation',
    text='+',    font='Arial',
    pos=[0, 0], height=1.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "runEnd"
runEndClock = core.Clock()
breakText = visual.TextStim(win=win, ori=0, name='breakText',
    text=u'You finished this round!',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)


# Initialize components for Routine "End"
EndClock = core.Clock()
endTask = visual.TextStim(win=win, ori=0, name='endTask',
    text=u'Congratulations! You finished the game!',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Welcome"-------
t = 0
WelcomeClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
advanceScreen = event.BuilderKeyResponse()  # create an object of type KeyResponse
advanceScreen.status = NOT_STARTED
# keep track of which components have finished
WelcomeComponents = []
WelcomeComponents.append(welcomeScreen)
WelcomeComponents.append(advanceScreen)
WelcomeComponents.append(polygon)
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Welcome"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeScreen* updates
    if t >= 0.0 and welcomeScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        welcomeScreen.tStart = t  # underestimates by a little under one frame
        welcomeScreen.frameNStart = frameN  # exact frame index
        welcomeScreen.setAutoDraw(True)
    
    # *advanceScreen* updates
    if t >= 0.0 and advanceScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        advanceScreen.tStart = t  # underestimates by a little under one frame
        advanceScreen.frameNStart = frameN  # exact frame index
        advanceScreen.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if advanceScreen.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t  # underestimates by a little under one frame
        polygon.frameNStart = frameN  # exact frame index
        polygon.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Directions"-------
t = 0
DirectionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED

# keep track of which components have finished
DirectionsComponents = []
DirectionsComponents.append(direction1)
DirectionsComponents.append(key_resp_2)
for thisComponent in DirectionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Directions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = DirectionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *direction1* updates
    if t >= 0.0 and direction1.status == NOT_STARTED:
        # keep track of start time/frame for later
        direction1.tStart = t  # underestimates by a little under one frame
        direction1.frameNStart = frameN  # exact frame index
        direction1.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DirectionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Directions"-------
for thisComponent in DirectionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Directions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "directions2"-------
t = 0
directions2Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_3.status = NOT_STARTED
# keep track of which components have finished
directions2Components = []
directions2Components.append(key_resp_3)
directions2Components.append(directionsText2)
for thisComponent in directions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "directions2"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = directions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # underestimates by a little under one frame
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *directionsText2* updates
    if t >= 0.0 and directionsText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        directionsText2.tStart = t  # underestimates by a little under one frame
        directionsText2.frameNStart = frameN  # exact frame index
        directionsText2.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in directions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "directions2"-------
for thisComponent in directions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "directions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/PlanetRuns.xlsx'),
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisRun.rgb)
if thisRun != None:
    for paramName in thisRun.keys():
        exec(paramName + '= thisRun.' + paramName)

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun.keys():
            exec(paramName + '= thisRun.' + paramName)
    
    #------Prepare to start Routine "trigger"-------
    t = 0
    triggerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    receiveTrigger = event.BuilderKeyResponse()  # create an object of type KeyResponse
    receiveTrigger.status = NOT_STARTED
    # keep track of which components have finished
    triggerComponents = []
    triggerComponents.append(waitForTrigger)
    triggerComponents.append(receiveTrigger)
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trigger"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = triggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *waitForTrigger* updates
        if t >= 0.0 and waitForTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            waitForTrigger.tStart = t  # underestimates by a little under one frame
            waitForTrigger.frameNStart = frameN  # exact frame index
            waitForTrigger.setAutoDraw(True)
        
        # *receiveTrigger* updates
        if t >= 0.0 and receiveTrigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            receiveTrigger.tStart = t  # underestimates by a little under one frame
            receiveTrigger.frameNStart = frameN  # exact frame index
            receiveTrigger.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if receiveTrigger.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trigger"-------
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "waitForScanner"-------
    t = 0
    waitForScannerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    #if expInfo['mriMode'] != 'Off':
    #    if trigger == 'usb':
    #        vol = launchScan(win, MR_settings, 
    #              globalClock=fmriClock, 
    #              mode=expInfo['mriMode'])
    #        if ser: # for GSR sync
    #            ser.writeUSB(0,1)  # Raise BNC
    #            ser.writeUSB(1,int('11111111',2))  # Raise all pins for Parallel
    
    #    elif trigger == 'parallel':
    #        address = 0x378
    #        #parallel.setPortAddress(0x378)
    #        wait_msg = "Get Ready!"
    #        pinStatus = winioport.inp(address)
    #        waitMsgStim = visual.TextStim(win, color='white', text=wait_msg)
    #        waitMsgStim.draw()
    #        win.flip()
    #        while True:
    #            if pinStatus != winioport.inp(address):
    #               break
                   # start exp when pin values change
    #        fmriClock.reset()
    #        logging.exp('parallel trigger: start of scan')
    #        win.flip()  # blank the screen on first sync pulse received
    
    #expInfo['triggerWallTime'] = time.ctime()
    
    runs.addData('TaskVersion', runOrderFile)
    # keep track of which components have finished
    waitForScannerComponents = []
    for thisComponent in waitForScannerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "waitForScanner"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = waitForScannerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in waitForScannerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "waitForScanner"-------
    for thisComponent in waitForScannerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    routineTimer.reset()
    
    # the Routine "waitForScanner" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    blocks = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(runOrderFile),
        seed=None, name='blocks')
    thisExp.addLoop(blocks)  # add the loop to the experiment
    thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock.keys():
            exec(paramName + '= thisBlock.' + paramName)
    
    for thisBlock in blocks:
        currentLoop = blocks
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock.keys():
                exec(paramName + '= thisBlock.' + paramName)
        
        #------Prepare to start Routine "trial_cue"-------
        t = 0
        trial_cueClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if Run=='Run1':
            valueConditions=ValueCondition1
        if Run=='Run2':
            valueConditions=ValueCondition2
        if Run=='Run3':
            valueConditions=ValueCondition3
        if Run=='Run4':
            valueConditions=ValueCondition4
        
        
        
        # Set Cue image on Reward Value Condition
        if (valueConditions == 'Low1') or (valueConditions == 'Low2') or (valueConditions == 'Low3') or (valueConditions == 'Low4') or (valueConditions == 'Low5') or (valueConditions=='Low6'):
            valueCondition='low'
            cueImage = 'low.png'
        else:
            valueCondition='high'
            cueImage = 'high.png'
        # set border width of 2nd border frame
        if valueCondition == 'low':
             borderColor='black'
        else:
             borderColor='white'
        frame2.setLineColor(borderColor)
        
        
        
        
        #cueTimeAdded = False
        currentLoop.addData('blockOnset', fmriClock.getTime())
        currentLoop.addData('cueOnset', fmriClock.getTime())
        Cue2.setImage(os.path.join('images',cueImage))
        ISIs=copy.copy(allISIs)
        random.shuffle(ISIs)
        AllRotations=copy.copy(rotations)
        random.shuffle(AllRotations)
        blockClock.reset()
        # keep track of which components have finished
        trial_cueComponents = []
        trial_cueComponents.append(Cue2)
        trial_cueComponents.append(frame1)
        trial_cueComponents.append(frame2)
        trial_cueComponents.append(drawCircle)
        for thisComponent in trial_cueComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial_cue"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trial_cueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            #if not cueTimeAdded:
            #    currentLoop.addData('blockOnset', fmriClock.getTime())
            #    currentLoop.addData('cueOnset', fmriClock.getTime())
            #    cueTimeAdded = True
            
            # *Cue2* updates
            if t >= 0.0 and Cue2.status == NOT_STARTED:
                # keep track of start time/frame for later
                Cue2.tStart = t  # underestimates by a little under one frame
                Cue2.frameNStart = frameN  # exact frame index
                Cue2.setAutoDraw(True)
            if Cue2.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                Cue2.setAutoDraw(False)
            
            # *frame1* updates
            if t >= 0.0 and frame1.status == NOT_STARTED:
                # keep track of start time/frame for later
                frame1.tStart = t  # underestimates by a little under one frame
                frame1.frameNStart = frameN  # exact frame index
                frame1.setAutoDraw(True)
            if frame1.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                frame1.setAutoDraw(False)
            
            # *frame2* updates
            if t >= 0.0 and frame2.status == NOT_STARTED:
                # keep track of start time/frame for later
                frame2.tStart = t  # underestimates by a little under one frame
                frame2.frameNStart = frameN  # exact frame index
                frame2.setAutoDraw(True)
            if frame2.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                frame2.setAutoDraw(False)
            
            
            
            # *drawCircle* updates
            if t >= 0.0 and drawCircle.status == NOT_STARTED:
                # keep track of start time/frame for later
                drawCircle.tStart = t  # underestimates by a little under one frame
                drawCircle.frameNStart = frameN  # exact frame index
                drawCircle.setAutoDraw(True)
            if drawCircle.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                drawCircle.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial_cue"-------
        for thisComponent in trial_cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('valueConditions', valueConditions)
        blocks.addData('valueCondition', valueCondition)
        blocks.addData('cueImage', cueImage)
        currentLoop.addData('cueOffset', fmriClock.getTime())
        
        
        
        
        #------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # set border color of 2nd border frame
        if valueCondition == 'low':
             borderColor='black'
        else:
             borderColor='white'
        fixationFrame2.setLineColor(borderColor)
        
        
        
        fixation1.setColor('white', colorSpace='rgb')
        fixation1.setText('+')
        # keep track of which components have finished
        fixationComponents = []
        fixationComponents.append(fixation1)
        fixationComponents.append(fixationFrame1)
        fixationComponents.append(fixationFrame2)
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "fixation"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *fixation1* updates
            if t >= 0 and fixation1.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation1.tStart = t  # underestimates by a little under one frame
                fixation1.frameNStart = frameN  # exact frame index
                fixation1.setAutoDraw(True)
            if fixation1.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixation1.setAutoDraw(False)
            
            # *fixationFrame1* updates
            if t >= 0.0 and fixationFrame1.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationFrame1.tStart = t  # underestimates by a little under one frame
                fixationFrame1.frameNStart = frameN  # exact frame index
                fixationFrame1.setAutoDraw(True)
            if fixationFrame1.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixationFrame1.setAutoDraw(False)
            
            # *fixationFrame2* updates
            if t >= 0.0 and fixationFrame2.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationFrame2.tStart = t  # underestimates by a little under one frame
                fixationFrame2.frameNStart = frameN  # exact frame index
                fixationFrame2.setAutoDraw(True)
            if fixationFrame2.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                fixationFrame2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(colorTrialsFile),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        for thisTrial in trials:
            currentLoop = trials
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial.keys():
                    exec(paramName + '= thisTrial.' + paramName)
            
            #------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock 
            frameN = -1
            routineTimer.add(0.500000)
            # update component parameters for each repeat
            ISI=ISIs.pop()
            rotation=AllRotations.pop()
            if valueConditions=="Low1":
                targetColor=LowColors1
                targetType=TrialType1
                prepot=Prepot1
                GoPrepot=GoPrepot1
                stimPic=LowStimPic1
            elif valueConditions=="High1":
                targetColor=HighColors1
                targetType=TrialType1
                prepot=Prepot1
                GoPrepot=GoPrepot1
                stimPic=HighStimPic1
            if valueConditions=="Low2":
                targetColor=LowColors2
                targetType=TrialType2
                prepot=Prepot2
                GoPrepot=GoPrepot2
                stimPic=LowStimPic2
            elif valueConditions=="High2":
                targetColor=HighColors2
                targetType=TrialType2
                prepot=Prepot2
                GoPrepot=GoPrepot2
                stimPic=HighStimPic2
            if valueConditions=="Low3":
                targetColor=LowColors3
                targetType=TrialType3
                prepot=Prepot3
                GoPrepot=GoPrepot3
                stimPic=LowStimPic3
            elif valueConditions=="High3":
                targetColor=HighColors3
                targetType=TrialType3
                prepot=Prepot3
                GoPrepot=GoPrepot3
                stimPic=HighStimPic3
            if valueConditions=="Low4":
                targetColor=LowColors4
                targetType=TrialType4
                prepot=Prepot4
                GoPrepot=GoPrepot4
                stimPic=LowStimPic4
            elif valueConditions=="High4":
                targetColor=HighColors4
                targetType=TrialType4
                prepot=Prepot4
                GoPrepot=GoPrepot4
                stimPic=HighStimPic4
            if valueConditions=="Low5":
                targetColor=LowColors5
                targetType=TrialType5
                prepot=Prepot5
                GoPrepot=GoPrepot5
                stimPic=HighStimPic5
            elif valueConditions=="High5":
                targetColor=HighColors5
                targetType=TrialType5
                prepot=Prepot5
                GoPrepot=GoPrepot5
                stimPic=HighStimPic5
            if valueConditions=="Low6":
                targetColor=LowColors6
                targetType=TrialType6
                prepot=Prepot6
                GoPrepot=GoPrepot6
                stimPic=LowStimPic6
            elif valueConditions=="High6":
                targetColor=HighColors6
                targetType=TrialType6
                prepot=Prepot6
                GoPrepot=GoPrepot6
                stimPic=HighStimPic6
            #targetImage=stimPic
            
            # Set Target Image on Go/Nogo Condition
            if expInfo['hand'] == 'right':
                if targetType == 'go':
                  correct =  '1'
                else:
                  correct = None
            else: # if hand='left'
                if targetType == 'go':
                  correct =  '6'
                else:
                  correct = None
            
            # set border color of 2nd border frame
            if valueCondition == 'low':
                 borderColor='black'
            else:
                 borderColor='white'
            trialFrame2.setLineColor(borderColor)
            
            
            Target.setOri(rotation)
            Target.setImage(os.path.join('images',stimPic))
            targetResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            targetResp.status = NOT_STARTED
            trials.addData('targetOnset', fmriClock.getTime())
            
            #targetTimeAdded= False
            
            # keep track of which components have finished
            trialComponents = []
            trialComponents.append(trialFrame)
            trialComponents.append(trialFrame2)
            trialComponents.append(Target)
            trialComponents.append(targetResp)
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "trial"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                
                
                
                
                # *trialFrame* updates
                if t >= 0 and trialFrame.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    trialFrame.tStart = t  # underestimates by a little under one frame
                    trialFrame.frameNStart = frameN  # exact frame index
                    trialFrame.setAutoDraw(True)
                if trialFrame.status == STARTED and t >= (0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    trialFrame.setAutoDraw(False)
                
                # *trialFrame2* updates
                if t >= 0 and trialFrame2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    trialFrame2.tStart = t  # underestimates by a little under one frame
                    trialFrame2.frameNStart = frameN  # exact frame index
                    trialFrame2.setAutoDraw(True)
                if trialFrame2.status == STARTED and t >= (0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    trialFrame2.setAutoDraw(False)
                
                # *Target* updates
                if t >= 0 and Target.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Target.tStart = t  # underestimates by a little under one frame
                    Target.frameNStart = frameN  # exact frame index
                    Target.setAutoDraw(True)
                if Target.status == STARTED and t >= (0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    Target.setAutoDraw(False)
                
                # *targetResp* updates
                if t >= 0 and targetResp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    targetResp.tStart = t  # underestimates by a little under one frame
                    targetResp.frameNStart = frameN  # exact frame index
                    targetResp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(targetResp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if targetResp.status == STARTED and t >= (0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                    targetResp.status = STOPPED
                if targetResp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if targetResp.keys == []:  # then this was the first keypress
                            targetResp.keys = theseKeys[0]  # just the first key pressed
                            targetResp.rt = targetResp.clock.getTime()
                            # was this 'correct'?
                            if (targetResp.keys == str(correct)) or (targetResp.keys == correct):
                                targetResp.corr = 1
                            else:
                                targetResp.corr = 0
                #if not targetTimeAdded:
                #    currentLoop.addData('targetOnset', fmriClock.getTime())
                #    targetTimeAdded = True
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials.addData('ISI', ISI)
            
            
            trials.addData('valueCondition', valueCondition)
            #trials.addData('targetImage', targetImage)
            trials.addData('targetColor', targetColor)
            trials.addData('stimRotation', rotation)
            trials.addData('thisTargetType', targetType)
            trials.addData('thisTrialNoGoPrepot', prepot)
            trials.addData('thisTrialGoPrepot', GoPrepot)
            
            # check responses
            if targetResp.keys in ['', [], None]:  # No response was made
               targetResp.keys=None
               # was no response the correct answer?!
               if str(correct).lower() == 'none': targetResp.corr = 1  # correct non-response
               else: targetResp.corr = 0  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('targetResp.keys',targetResp.keys)
            trials.addData('targetResp.corr', targetResp.corr)
            if targetResp.keys != None:  # we had a response
                trials.addData('targetResp.rt', targetResp.rt)
            trials.addData('targetOffset', fmriClock.getTime())
            
            #------Prepare to start Routine "jitter"-------
            t = 0
            jitterClock.reset()  # clock 
            frameN = -1
            # update component parameters for each repeat
            # set border color of 2nd border frame
            if valueCondition == 'low':
                 borderColor='black'
            else:
                 borderColor='white'
            jitterFrame2.setLineColor(borderColor)
            
            # Set Target Image on Go/Nogo Condition
            if expInfo['hand'] == 'right':
                if targetType == 'go':
                  correct =  '1'
                else:
                  correct = None
            else: # if hand='left'
                if targetType == 'go':
                  correct =  '6'
                else:
                  correct = None
            lateResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
            lateResp.status = NOT_STARTED
            
            
            # keep track of which components have finished
            jitterComponents = []
            jitterComponents.append(jitteredISI)
            jitterComponents.append(jitterFrame1)
            jitterComponents.append(jitterFrame2)
            jitterComponents.append(lateResp)
            for thisComponent in jitterComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "jitter"-------
            continueRoutine = True
            while continueRoutine:
                # get current time
                t = jitterClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *jitteredISI* updates
                if t >= 0.0 and jitteredISI.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    jitteredISI.tStart = t  # underestimates by a little under one frame
                    jitteredISI.frameNStart = frameN  # exact frame index
                    jitteredISI.setAutoDraw(True)
                if jitteredISI.status == STARTED and t >= (0.0 + (ISI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    jitteredISI.setAutoDraw(False)
                
                # *jitterFrame1* updates
                if t >= 0.0 and jitterFrame1.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    jitterFrame1.tStart = t  # underestimates by a little under one frame
                    jitterFrame1.frameNStart = frameN  # exact frame index
                    jitterFrame1.setAutoDraw(True)
                if jitterFrame1.status == STARTED and t >= (0.0 + (ISI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    jitterFrame1.setAutoDraw(False)
                
                # *jitterFrame2* updates
                if t >= 0.0 and jitterFrame2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    jitterFrame2.tStart = t  # underestimates by a little under one frame
                    jitterFrame2.frameNStart = frameN  # exact frame index
                    jitterFrame2.setAutoDraw(True)
                if jitterFrame2.status == STARTED and t >= (0.0 + (ISI-win.monitorFramePeriod*0.75)): #most of one frame period left
                    jitterFrame2.setAutoDraw(False)
                
                
                # *lateResp* updates
                if t >= 0.0 and lateResp.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    lateResp.tStart = t  # underestimates by a little under one frame
                    lateResp.frameNStart = frameN  # exact frame index
                    lateResp.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(lateResp.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if lateResp.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                    lateResp.status = STOPPED
                if lateResp.status == STARTED:
                    theseKeys = event.getKeys(keyList=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        if lateResp.keys == []:  # then this was the first keypress
                            lateResp.keys = theseKeys[0]  # just the first key pressed
                            lateResp.rt = lateResp.clock.getTime()
                            # was this 'correct'?
                            if (lateResp.keys == str(correct)) or (lateResp.keys == correct):
                                lateResp.corr = 1
                            else:
                                lateResp.corr = 0
                # write outcome text
                if targetResp.keys: # if a response is made during planet presentation
                  if targetResp.corr==1: 
                        if valueCondition == 'low':
                            outcomeText = '+ $0.20'
                            outcomeNumber=0.20
                        else:  # valueCondition == 'high'
                            outcomeText = '+ $1.00'
                            outcomeNumber=1.00
                  else: # if targetResp.corr=0
                    if targetType=='nogo':
                        if valueCondition == 'low':
                            outcomeText = '- $0.10'
                            outcomeNumber= -0.10
                        else:  # valueCondition == 'high'
                            outcomeText = '- $0.50'
                            outcomeNumber= -0.50
                
                if not targetResp.keys: # if no response is made during planet presentation
                  if  targetType=='go':
                    if lateResp.corr==1: # if correct late response
                        if valueCondition == 'low':
                            outcomeText = '+ $0.20'
                            outcomeNumber=0.20
                        else:  # valueCondition == 'high'
                            outcomeText = '+ $1.00'
                            outcomeNumber=1.00 
                    else: # if no response is made
                        if valueCondition == 'low':
                            outcomeText = '- $0.10'
                            outcomeNumber= -0.10
                        else:  # valueCondition == 'high'
                            outcomeText = '- $0.50'
                            outcomeNumber= -0.50
                
                  elif targetType == 'nogo': # if no response is made for a nogo trial
                    if lateResp.rt>1.5:
                        if valueCondition == 'low':
                            outcomeText = '+ $0.20'
                            outcomeNumber=0.20
                        else: # if high
                            outcomeText = '+ $1.00'
                            outcomeNumber=1.00
                    else: # if a late response is made for a nogo
                        if valueCondition == 'low':
                            outcomeText = '- $0.10'
                            outcomeNumber= -0.10
                        else:  # valueCondition == 'high'
                            outcomeText = '- $0.50'
                            outcomeNumber= -0.50
                
                
                # label accuracy including late responses
                if outcomeNumber==1.00 or outcomeNumber==0.20:
                    Accuracy=1
                else:
                    Accuracy=0
                
                if targetResp.keys:
                    RT=targetResp.rt
                else:
                    RT=np.add(lateResp.rt, 0.5)
                #    RT=0.5 + (lateResp.rt)
                
                if targetType=='go':
                    goRT=RT
                else:
                    goRT='nan'
                
                
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in jitterComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "jitter"-------
            for thisComponent in jitterComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # check responses
            if lateResp.keys in ['', [], None]:  # No response was made
               lateResp.keys=None
               # was no response the correct answer?!
               if str(correct).lower() == 'none': lateResp.corr = 1  # correct non-response
               else: lateResp.corr = 0  # failed to respond (incorrectly)
            # store data for trials (TrialHandler)
            trials.addData('lateResp.keys',lateResp.keys)
            trials.addData('lateResp.corr', lateResp.corr)
            if lateResp.keys != None:  # we had a response
                trials.addData('lateResp.rt', lateResp.rt)
            trials.addData('Accuracy', Accuracy)
            trials.addData('outcomeText', outcomeText)
            trials.addData('outcomeNumber', outcomeNumber)
            trials.addData('RT', RT)
            trials.addData('goRT', goRT)
            # the Routine "jitter" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'trials'
        
        
        #------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # set border color of 2nd border frame
        if valueCondition == 'low':
             borderColor='black'
        else:
             borderColor='white'
        rewardFrame2.setLineColor(borderColor)
        
        # calculate reward total
        outcomeTotal = trials.data['outcomeNumber'].sum()
        if outcomeTotal >= 0:
           if outcomeTotal == 0:
            outcomeType='got'
           else:
            outcomeType='won'
        if outcomeTotal<0:
           outcomeType='lost'
        
        if outcomeType=='won':
            rewardColor='lawngreen'
        else:
            rewardColor='orangered'
        
        outcomeDisplay=abs(outcomeTotal)
        msg = "You %s $%s0!" %(outcomeType, outcomeDisplay)
        
        reward.setColor(rewardColor, colorSpace='rgb')
        reward.setText(msg)
        blocks.addData('feedbackOnset', fmriClock.getTime())
        # keep track of which components have finished
        feedbackComponents = []
        feedbackComponents.append(reward)
        feedbackComponents.append(rewardFrame1)
        feedbackComponents.append(rewardFrame2)
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *reward* updates
            if t >= 0 and reward.status == NOT_STARTED:
                # keep track of start time/frame for later
                reward.tStart = t  # underestimates by a little under one frame
                reward.frameNStart = frameN  # exact frame index
                reward.setAutoDraw(True)
            if reward.status == STARTED and t >= (0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                reward.setAutoDraw(False)
            
            # *rewardFrame1* updates
            if t >= 0.0 and rewardFrame1.status == NOT_STARTED:
                # keep track of start time/frame for later
                rewardFrame1.tStart = t  # underestimates by a little under one frame
                rewardFrame1.frameNStart = frameN  # exact frame index
                rewardFrame1.setAutoDraw(True)
            if rewardFrame1.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                rewardFrame1.setAutoDraw(False)
            
            # *rewardFrame2* updates
            if t >= 0.0 and rewardFrame2.status == NOT_STARTED:
                # keep track of start time/frame for later
                rewardFrame2.tStart = t  # underestimates by a little under one frame
                rewardFrame2.frameNStart = frameN  # exact frame index
                rewardFrame2.setAutoDraw(True)
            if rewardFrame2.status == STARTED and t >= (0.0 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                rewardFrame2.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('outcomeTotal', outcomeTotal)
        blocks.addData('feedbackOffset', fmriClock.getTime())
        
        #------Prepare to start Routine "endBlock"-------
        t = 0
        endBlockClock.reset()  # clock 
        frameN = -1
        routineTimer.add(10.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        endBlockComponents = []
        endBlockComponents.append(breakFixation)
        for thisComponent in endBlockComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "endBlock"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = endBlockClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *breakFixation* updates
            if t >= 0.0 and breakFixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                breakFixation.tStart = t  # underestimates by a little under one frame
                breakFixation.frameNStart = frameN  # exact frame index
                breakFixation.setAutoDraw(True)
            if breakFixation.status == STARTED and t >= (0.0 + (10-win.monitorFramePeriod*0.75)): #most of one frame period left
                breakFixation.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in endBlockComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "endBlock"-------
        for thisComponent in endBlockComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        blocks.addData('blockOffset', fmriClock.getTime())
        thisExp.nextEntry()
        
    # completed 1 repeats of 'blocks'
    
    
    #------Prepare to start Routine "runEnd"-------
    t = 0
    runEndClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    SpaceToEndRun = event.BuilderKeyResponse()  # create an object of type KeyResponse
    SpaceToEndRun.status = NOT_STARTED
    runs.addData('runOffset', fmriClock.getTime())
    # keep track of which components have finished
    runEndComponents = []
    runEndComponents.append(breakText)
    runEndComponents.append(SpaceToEndRun)
    for thisComponent in runEndComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "runEnd"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = runEndClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *breakText* updates
        if t >= 0 and breakText.status == NOT_STARTED:
            # keep track of start time/frame for later
            breakText.tStart = t  # underestimates by a little under one frame
            breakText.frameNStart = frameN  # exact frame index
            breakText.setAutoDraw(True)
        
        # *SpaceToEndRun* updates
        if t >= 0 and SpaceToEndRun.status == NOT_STARTED:
            # keep track of start time/frame for later
            SpaceToEndRun.tStart = t  # underestimates by a little under one frame
            SpaceToEndRun.frameNStart = frameN  # exact frame index
            SpaceToEndRun.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if SpaceToEndRun.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in runEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "runEnd"-------
    for thisComponent in runEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "runEnd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'runs'


#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
SpaceToExit = event.BuilderKeyResponse()  # create an object of type KeyResponse
SpaceToExit.status = NOT_STARTED
# keep track of which components have finished
EndComponents = []
EndComponents.append(endTask)
EndComponents.append(SpaceToExit)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endTask* updates
    if t >= 0 and endTask.status == NOT_STARTED:
        # keep track of start time/frame for later
        endTask.tStart = t  # underestimates by a little under one frame
        endTask.frameNStart = frameN  # exact frame index
        endTask.setAutoDraw(True)
    
    # *SpaceToExit* updates
    if t >= 0 and SpaceToExit.status == NOT_STARTED:
        # keep track of start time/frame for later
        SpaceToExit.tStart = t  # underestimates by a little under one frame
        SpaceToExit.frameNStart = frameN  # exact frame index
        SpaceToExit.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if SpaceToExit.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#ser.writeUSB(0,0)
#ser.writeUSB(1,0)
#ser.close()
#win.close()
#core.quit()



















# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
