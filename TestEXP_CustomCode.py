# IMPORT STATEMENTS

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

#Make sure you are in the correct directory
os.chdir('/home/melian/Documents/BrainLock')

#IMPORT CUSTOM MODULES
from Password_Setup import *

#PRE-LOAD STIMS
Random_Words = ['goodbye','hola','bonjour']

#Initial Password Input

passfinal = 'hi' #passwordsetup()

#INTRO SCREEN
win = visual.Window(size=(500, 500), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

#CREATE TEXT OBJECTS 
Password = visual.TextStim(win=win, ori=0, name='Password',
    text=passfinal,font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=300,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

Random_0 = visual.TextStim(win=win, ori=0, name='Random_2',
    text=Random_Words[0],    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

Random_1 = visual.TextStim(win=win, ori=0, name='Random_1',
    text=Random_Words[1],    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

Random_2 = visual.TextStim(win=win, ori=0, name='Random_1',
    text=Random_Words[2],    font=u'Arial',
    pos=[0, 0], height=0.5, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

fixation = visual.GratingStim(win=win, mask='cross', size=0.5, pos=[0,0], sf=0.1)

sync = visual.ShapeStim(win, units='', lineWidth=1.5, lineColor='white', 
    lineColorSpace='rgb', fillColor='white', fillColorSpace='rgb', 
    vertices=((0.8, 0.9), (0.9, 0.9), (0.9, 0.8), (0.8,0.8)),
    closeShape=True, pos=(0, 0), size=1, ori=0.0, opacity=1.0, 
    contrast=1.0, depth=0, interpolate=True, name=None, 
    autoLog=None, autoDraw=False)

fixation.draw()
win.flip()

all_text = [Password,Random_0,Random_1,Random_2]

#DATA ACQUISTION LOOP

#raw_input("enter to start")

for i in range(10):
    
    text = all_text[i % 4]

    for frameN in range(200):

        if 0 <= frameN < 50:
            fixation.draw()
        if 50 <= frameN < 150:    
            text.draw()
            sync.draw()
        if 150 <= frameN < 200:
            fixation.draw()


        win.flip()

win.close()


