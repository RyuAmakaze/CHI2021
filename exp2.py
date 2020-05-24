#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 5月 10, 2020, at 11:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLatencyMode'] = '4'
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard
import random


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Yu Yamaoka\\Desktop\\DC関係\\test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[2560, 1440], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
basic = visual.TextStim(win=win, name='basic',
    text='+  +  +',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);
hidari = sound.Sound('sound/hidari.wav', secs=0.4, stereo=True, hamming=True,
    name='hidari')
hidari.setVolume(1)
migi = sound.Sound('sound/migi.wav', secs=0.4, stereo=True, hamming=False,
    name='migi')
migi.setVolume(1)
right = visual.TextStim(win=win, name='right',
    text='        +',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='red', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-3.0);
left = visual.TextStim(win=win, name='left',
    text='+        ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='red', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=-4.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=10, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials

    #exp_code,0:right -200ms,1:right +200ms,2:left -200ms,3:left +200ms
    exp_code = random.randrange(4)
    print(exp_code)

    if(exp_code==0)or(exp_code==2):
        app_time = 2.4 - 0.2

    if(exp_code==1)or(exp_code==3):
        app_time = 2.4 + 0.2

    # #######################################################################

    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    routineTimer.add(5.310000)
    # update component parameters for each repeat
    hidari.setSound('sound/hidari.wav', secs=0.4, hamming=True)
    hidari.setVolume(1, log=False)
    migi.setSound('sound/migi.wav', secs=0.4, hamming=False)
    migi.setVolume(1, log=False)
    # keep track of which components have finished
    trialComponents = [basic, hidari, migi, right, left]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *basic* updates
        if basic.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            basic.frameNStart = frameN  # exact frame index
            basic.tStart = t  # local t and not account for scr refresh
            basic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(basic, 'tStartRefresh')  # time at next scr refresh
            basic.setAutoDraw(True)
        if basic.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > basic.tStartRefresh + app_time-frameTolerance:
                # keep track of stop time/frame for later
                basic.tStop = t  # not accounting for scr refresh
                basic.frameNStop = frameN  # exact frame index
                win.timeOnFlip(basic, 'tStopRefresh')  # time at next scr refresh
                basic.setAutoDraw(False)
        # start/stop hidari
        if(exp_code==2)or(exp_code==3):
            if hidari.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                hidari.frameNStart = frameN  # exact frame index
                hidari.tStart = t  # local t and not account for scr refresh
                hidari.tStartRefresh = tThisFlipGlobal  # on global time
                hidari.play(when=win)  # sync with win flip
            if hidari.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hidari.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    hidari.tStop = t  # not accounting for scr refresh
                    hidari.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(hidari, 'tStopRefresh')  # time at next scr refresh
                    hidari.stop()
        # start/stop migi
        if(exp_code==0)or(exp_code==1):
            if migi.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                migi.frameNStart = frameN  # exact frame index
                migi.tStart = t  # local t and not account for scr refresh
                migi.tStartRefresh = tThisFlipGlobal  # on global time
                migi.play(when=win)  # sync with win flip
            if migi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > migi.tStartRefresh + 0.4-frameTolerance:
                    # keep track of stop time/frame for later
                    migi.tStop = t  # not accounting for scr refresh
                    migi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(migi, 'tStopRefresh')  # time at next scr refresh
                    migi.stop()

        # *right* updates
        if(exp_code==0)or(exp_code==1):
            if right.status == NOT_STARTED and tThisFlip >= app_time-frameTolerance:
                # keep track of start time/frame for later
                right.frameNStart = frameN  # exact frame index
                right.tStart = t  # local t and not account for scr refresh
                right.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(right, 'tStartRefresh')  # time at next scr refresh
                right.setAutoDraw(True)
            if right.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > right.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    right.tStop = t  # not accounting for scr refresh
                    right.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(right, 'tStopRefresh')  # time at next scr refresh
                    right.setAutoDraw(False)

        # *left* updates
        if(exp_code==2)or(exp_code==3):
            if left.status == NOT_STARTED and tThisFlip >= app_time-frameTolerance:
                # keep track of start time/frame for later
                left.frameNStart = frameN  # exact frame index
                left.tStart = t  # local t and not account for scr refresh
                left.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(left, 'tStartRefresh')  # time at next scr refresh
                left.setAutoDraw(True)
            if left.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > left.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    left.tStop = t  # not accounting for scr refresh
                    left.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(left, 'tStopRefresh')  # time at next scr refresh
                    left.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('basic.started', basic.tStartRefresh)
    trials.addData('basic.stopped', basic.tStopRefresh)
    hidari.stop()  # ensure sound has stopped at end of routine
    trials.addData('hidari.started', hidari.tStartRefresh)
    trials.addData('hidari.stopped', hidari.tStopRefresh)
    migi.stop()  # ensure sound has stopped at end of routine
    trials.addData('migi.started', migi.tStartRefresh)
    trials.addData('migi.stopped', migi.tStopRefresh)
    trials.addData('right.started', right.tStartRefresh)
    trials.addData('right.stopped', right.tStopRefresh)
    trials.addData('left.started', left.tStartRefresh)
    trials.addData('left.stopped', left.tStopRefresh)
    thisExp.nextEntry()

# completed 10 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
