#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), Tue Dec 19 17:17:58 2017
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
expName = 'PlanetPractice'  # from the Builder filename that created this script
expInfo = {u'session': u'prac', u'participant': u'PP'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/Katie/Dropbox/Planets/ForGithub/PracticeTask/PlanetPractice.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
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

# Initialize components for Routine "directions1"
directions1Clock = core.Clock()
text_8 = visual.TextStim(win=win, ori=0, name='text_8',
    text='You will be traveling through different galaxies. In one galaxy, you can win low amounts of money, but in the other you can win high amounts.\r\n\r\nIf you see a circle with 1 star, that means you can win or lose a low amount.\r\n\r\nIf you see a circle with 2 stars, that means you can win or lose a high amount. \r\n\r\nClick space to continue.',    font='Arial',
    pos=[-10, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
highCueImage = visual.ImageStim(win=win, name='highCueImage',
    image='images/high.png', mask=None,
    ori=0, pos=[10, -5], size=[9, 9],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
lowCueImage = visual.ImageStim(win=win, name='lowCueImage',
    image='images/low.png', mask=None,
    ori=0, pos=[10, 6], size=[9, 9],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
lowLabel = visual.TextStim(win=win, ori=0, name='lowLabel',
    text='Low',    font='Arial',
    pos=[13.5, 10], height=.8, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
highLabel = visual.TextStim(win=win, ori=0, name='highLabel',
    text='High',    font='Arial',
    pos=[13.5, -.5], height=.8, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)
polygon = visual.Rect(win=win, name='polygon',
    width=[10, 10][0], height=[10, 10][1],
    ori=0, pos=[10, 6],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-6.0, 
interpolate=True)
polygon_2 = visual.Rect(win=win, name='polygon_2',
    width=[10, 10][0], height=[10, 10][1],
    ori=0, pos=[10, -5],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-7.0, 
interpolate=True)
polygon_3 = visual.Rect(win=win, name='polygon_3',
    width=[10.5, 10.5][0], height=[10.5, 10.5][1],
    ori=0, pos=[10, -5],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-8.0, 
interpolate=True)

# Initialize components for Routine "Directions_images"
Directions_imagesClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text='In this game, you will see planets and asteroids. Planets have craters, and asteroids have stripes. Only click for the planets! If it is a planet, click space as quickly as possible. If it is an asteroid, do not press anything.\r\n\r\n',    font='Arial',
    pos=[0, 5], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='images/crater_planet.png', mask=None,
    ori=0, pos=[-10, -3], size=[10, 10],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image_3 = visual.ImageStim(win=win, name='image_3',
    image='images/striped_planet.png', mask=None,
    ori=0, pos=[10, -3], size=[10, 10],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text='Planet',    font='Arial',
    pos=[-10, -9], height=1.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
text_7 = visual.TextStim(win=win, ori=0, name='text_7',
    text='Asteroid',    font='Arial',
    pos=[10, -9], height=1.5, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "directions2"
directions2Clock = core.Clock()
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='First you will see a cue that will tell you how much you can earn.\r\n\r\nNext you will see a planet or an asteroid. \r\n\r\nThen you will see how you did. If you did well, you will get a reward, but if you did not do well you will get punished. \r\n\r\nPress space to start the practice!',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
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

trialFrame = visual.Rect(win=win, name='trialFrame',
    width=[18, 18][0], height=[18, 18][1],
    ori=0, pos=[0, 0],
    lineWidth=2, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-1.0, 
interpolate=True)
trialFrame2 = visual.Rect(win=win, name='trialFrame2',
    width=[19, 19][0], height=[19, 19][1],
    ori=0, pos=[0, 0],
    lineWidth=2, lineColor='black', lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1,depth=-2.0, 
interpolate=True)
Cue_1 = visual.ImageStim(win=win, name='Cue_1',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[15, 15],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ISI_1 = visual.TextStim(win=win, ori=0, name='ISI_1',
    text='+',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
Target = visual.ImageStim(win=win, name='Target',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[15, 15],
    color=1.0, colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=256, interpolate=True, depth=-5.0)
ISI_2 = visual.TextStim(win=win, ori=0, name='ISI_2',
    text='+',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-7.0)
Reward_text = visual.TextStim(win=win, ori=0, name='Reward_text',
    text=None,    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-8.0)
ITI = visual.TextStim(win=win, ori=0, name='ITI',
    text='+',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-9.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='You finished the practice!\r\n\r\nIn the real game, you will only see the cue when the block starts, and you will only get feedback when you finish the block. Remember to go as fast as you can!\r\n\r\nIf you forget whether you are playing for low or high amounts, look at the boxes. One box means low, and two boxes mean high.\r\n\r\nDo you have any questions?',    font='Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "directions1"-------
t = 0
directions1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_7 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_7.status = NOT_STARTED
# keep track of which components have finished
directions1Components = []
directions1Components.append(key_resp_7)
directions1Components.append(text_8)
directions1Components.append(highCueImage)
directions1Components.append(lowCueImage)
directions1Components.append(lowLabel)
directions1Components.append(highLabel)
directions1Components.append(polygon)
directions1Components.append(polygon_2)
directions1Components.append(polygon_3)
for thisComponent in directions1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "directions1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = directions1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # underestimates by a little under one frame
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_7.keys = theseKeys[-1]  # just the last key pressed
            key_resp_7.rt = key_resp_7.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # underestimates by a little under one frame
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)
    
    # *highCueImage* updates
    if t >= 0.0 and highCueImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        highCueImage.tStart = t  # underestimates by a little under one frame
        highCueImage.frameNStart = frameN  # exact frame index
        highCueImage.setAutoDraw(True)
    
    # *lowCueImage* updates
    if t >= 0.0 and lowCueImage.status == NOT_STARTED:
        # keep track of start time/frame for later
        lowCueImage.tStart = t  # underestimates by a little under one frame
        lowCueImage.frameNStart = frameN  # exact frame index
        lowCueImage.setAutoDraw(True)
    
    # *lowLabel* updates
    if t >= 0.0 and lowLabel.status == NOT_STARTED:
        # keep track of start time/frame for later
        lowLabel.tStart = t  # underestimates by a little under one frame
        lowLabel.frameNStart = frameN  # exact frame index
        lowLabel.setAutoDraw(True)
    
    # *highLabel* updates
    if t >= 0.0 and highLabel.status == NOT_STARTED:
        # keep track of start time/frame for later
        highLabel.tStart = t  # underestimates by a little under one frame
        highLabel.frameNStart = frameN  # exact frame index
        highLabel.setAutoDraw(True)
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t  # underestimates by a little under one frame
        polygon.frameNStart = frameN  # exact frame index
        polygon.setAutoDraw(True)
    
    # *polygon_2* updates
    if t >= 0.0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t  # underestimates by a little under one frame
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.setAutoDraw(True)
    
    # *polygon_3* updates
    if t >= 0.0 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t  # underestimates by a little under one frame
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in directions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "directions1"-------
for thisComponent in directions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
   key_resp_7.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.nextEntry()
# the Routine "directions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Directions_images"-------
t = 0
Directions_imagesClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_6.status = NOT_STARTED
# keep track of which components have finished
Directions_imagesComponents = []
Directions_imagesComponents.append(text_5)
Directions_imagesComponents.append(image_2)
Directions_imagesComponents.append(image_3)
Directions_imagesComponents.append(key_resp_6)
Directions_imagesComponents.append(text_6)
Directions_imagesComponents.append(text_7)
for thisComponent in Directions_imagesComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Directions_images"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Directions_imagesClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *image_2* updates
    if t >= 0.0 and image_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_2.tStart = t  # underestimates by a little under one frame
        image_2.frameNStart = frameN  # exact frame index
        image_2.setAutoDraw(True)
    
    # *image_3* updates
    if t >= 0.0 and image_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_3.tStart = t  # underestimates by a little under one frame
        image_3.frameNStart = frameN  # exact frame index
        image_3.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # underestimates by a little under one frame
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_6.keys = theseKeys[-1]  # just the last key pressed
            key_resp_6.rt = key_resp_6.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # underestimates by a little under one frame
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # underestimates by a little under one frame
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Directions_imagesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Directions_images"-------
for thisComponent in Directions_imagesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
   key_resp_6.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.nextEntry()
# the Routine "Directions_images" was not non-slip safe, so reset the non-slip timer
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
directions2Components.append(text_4)
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
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # underestimates by a little under one frame
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
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
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
   key_resp_3.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "directions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions/practice.xlsx'),
    seed=0, name='trials')
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
    # update component parameters for each repeat
    
    
    
    # Set Cue image on Reward Value Condition
    if valueCondition == 'low':
        cueImage = 'low.png'
    else:
        cueImage = 'high.png'
    
    # Set Target Image on Go/Nogo Condition
    if targetType == 'go':
        targetImage = 'crater_planet.png'
        correct = 'space'
    else:
        targetImage = 'striped_planet.png'
        correct = None
    
    
    
    # set border width of 2nd border frame
    if valueCondition == 'low':
         borderColor='black'
    else:
         borderColor='white'
    trialFrame2.setLineColor(borderColor)
    
    # set outcome text
    outcomeText=None
    outcomeColor='white'
    Cue_1.setImage(os.path.join('images',cueImage))
    Target.setColor(targetcolor, colorSpace='rgb')
    Target.setImage(os.path.join('images',targetImage))
    key_resp_1 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_1.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(trialFrame)
    trialComponents.append(trialFrame2)
    trialComponents.append(Cue_1)
    trialComponents.append(ISI_1)
    trialComponents.append(Target)
    trialComponents.append(key_resp_1)
    trialComponents.append(ISI_2)
    trialComponents.append(Reward_text)
    trialComponents.append(ITI)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # write outcome text
        if key_resp_1.status == STOPPED and outcomeText == None:
            if check_correct(key_resp_1.keys,correct):
                if valueCondition == 'low':
                    outcomeText = 'Correct! + $0.20'
                    outcomeColor = 'green'
                else:  # valueCondition == 'high'
                    outcomeText = 'Correct! + $1.00'
                    outcomeColor='green'
            else:
              if valueCondition == 'low':
                    outcomeText = 'Incorrect! - $0.10'
                    outcomeColor='red'
              else:  # valueCondition == 'high'
                    outcomeText = 'Incorrect! - $0.50'
                    outcomeColor='red'
            Reward_text.setText(outcomeText)
            Reward_text.setColor(outcomeColor)
            trials.addData('outcomeText',outcomeText)
            trials.addData('cueImage', cueImage)
            trials.addData('targetImage', targetImage)
        
        # *trialFrame* updates
        if t >= 0 and trialFrame.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialFrame.tStart = t  # underestimates by a little under one frame
            trialFrame.frameNStart = frameN  # exact frame index
            trialFrame.setAutoDraw(True)
        if trialFrame.status == STARTED and (Reward_text.status==FINISHED):
            trialFrame.setAutoDraw(False)
        
        # *trialFrame2* updates
        if t >= 0 and trialFrame2.status == NOT_STARTED:
            # keep track of start time/frame for later
            trialFrame2.tStart = t  # underestimates by a little under one frame
            trialFrame2.frameNStart = frameN  # exact frame index
            trialFrame2.setAutoDraw(True)
        if trialFrame2.status == STARTED and (Reward_text.status==FINISHED):
            trialFrame2.setAutoDraw(False)
        
        # *Cue_1* updates
        if t >= 0 and Cue_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            Cue_1.tStart = t  # underestimates by a little under one frame
            Cue_1.frameNStart = frameN  # exact frame index
            Cue_1.setAutoDraw(True)
        if Cue_1.status == STARTED and t >= (0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            Cue_1.setAutoDraw(False)
        
        # *ISI_1* updates
        if (Cue_1.status==FINISHED) and ISI_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_1.tStart = t  # underestimates by a little under one frame
            ISI_1.frameNStart = frameN  # exact frame index
            ISI_1.setAutoDraw(True)
        if ISI_1.status == STARTED and t >= (ISI_1.tStart + ISI1):
            ISI_1.setAutoDraw(False)
        
        # *Target* updates
        if (ISI_1.status==FINISHED) and Target.status == NOT_STARTED:
            # keep track of start time/frame for later
            Target.tStart = t  # underestimates by a little under one frame
            Target.frameNStart = frameN  # exact frame index
            Target.setAutoDraw(True)
        if Target.status == STARTED and t >= (Target.tStart + 0.5):
            Target.setAutoDraw(False)
        
        # *key_resp_1* updates
        if (ISI_1.status==FINISHED) and key_resp_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_1.tStart = t  # underestimates by a little under one frame
            key_resp_1.frameNStart = frameN  # exact frame index
            key_resp_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_1.status == STARTED and t >= (key_resp_1.tStart + 1.5):
            key_resp_1.status = STOPPED
        if key_resp_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_1.keys == []:  # then this was the first keypress
                    key_resp_1.keys = theseKeys[0]  # just the first key pressed
                    key_resp_1.rt = key_resp_1.clock.getTime()
                    # was this 'correct'?
                    if (key_resp_1.keys == str(correct)) or (key_resp_1.keys == correct):
                        key_resp_1.corr = 1
                    else:
                        key_resp_1.corr = 0
        
        # *ISI_2* updates
        if (Target.status==FINISHED) and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_2.tStart = t  # underestimates by a little under one frame
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.setAutoDraw(True)
        if ISI_2.status == STARTED and t >= (ISI_2.tStart + 2):
            ISI_2.setAutoDraw(False)
        
        # *Reward_text* updates
        if (ISI_2.status==FINISHED) and Reward_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            Reward_text.tStart = t  # underestimates by a little under one frame
            Reward_text.frameNStart = frameN  # exact frame index
            Reward_text.setAutoDraw(True)
        if Reward_text.status == STARTED and t >= (Reward_text.tStart + 2):
            Reward_text.setAutoDraw(False)
        
        # *ITI* updates
        if (Reward_text.status==FINISHED) and ITI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ITI.tStart = t  # underestimates by a little under one frame
            ITI.frameNStart = frameN  # exact frame index
            ITI.setAutoDraw(True)
        if ITI.status == STARTED and t >= (ITI.tStart + 2):
            ITI.setAutoDraw(False)
        
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
    
    # check responses
    if key_resp_1.keys in ['', [], None]:  # No response was made
       key_resp_1.keys=None
       # was no response the correct answer?!
       if str(correct).lower() == 'none': key_resp_1.corr = 1  # correct non-response
       else: key_resp_1.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_1.keys',key_resp_1.keys)
    trials.addData('key_resp_1.corr', key_resp_1.corr)
    if key_resp_1.keys != None:  # we had a response
        trials.addData('key_resp_1.rt', key_resp_1.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_5.status = NOT_STARTED
# keep track of which components have finished
EndComponents = []
EndComponents.append(text_2)
EndComponents.append(key_resp_5)
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
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # underestimates by a little under one frame
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # underestimates by a little under one frame
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
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
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
   key_resp_5.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort() # or data files will save again on exit
win.close()
core.quit()
