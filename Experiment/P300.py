# IMPORT STATEMENTS

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
from random import random
import os  # handy system and path functions
import csv
import sys # to get file system encoding
from pylsl import StreamInlet, resolve_stream

#######  LSL Streaming
#print("looking for an EEG stream...")
#streams = resolve_stream('type','EEG')

# create a new inlet to read from the stream
#inlet = StreamInlet(streams[0])

#####


#####Getting the CSV File ready

#Make sure you are in the correct directory
os.chdir('/home/sydney/Brainlock')

#IMPORT CUSTOM MODULES
#from Password_Setup import *

#PRE-LOAD STIMS



##### Create a CSV with the person's name. This is the person's ID until we determine
    # how to do all the processing in python
usern=raw_input("Who you?")
fd = raw_input("random?")

#####

## PASWORD SETUP WILL BE IMPLEMENTED IN FUTURE VERSIONS
#Initial Password Input


#INTRO SCREEN
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

#CREATE NONTEXT OBJECTS 


fixation = visual.GratingStim(win=win, mask='cross', size=0.5, pos=[0,0], sf=0.1)

dot = visual.GratingStim(win=win, mask='circle', size=0.1, pos=[0,0], sf=0.1)


sync = visual.ShapeStim(win, units='', lineWidth=1.5, lineColor='white', 
    lineColorSpace='rgb', fillColor='white', fillColorSpace='rgb', 
    vertices=((0.8, 0.9), (0.9, 0.9), (0.9, 0.8), (0.8,0.8)),
    closeShape=True, pos=(0, 0), size=1, ori=0.0, opacity=1.0, 
    contrast=1.0, depth=0, interpolate=True, name=None, 
    autoLog=None, autoDraw=False)

#win.flip()

#DATA ACQUISTION LOOP

#raw_input("enter to start")


#60 = 1 second

#Set Flashing

with open(usern+'.csv','wb') as f:
    writer = csv.writer(f)

    for frameN in range(1800):

        
        if fd=="y":
            if frameN %180==0:
                ranval=randint(1,3)
                if ranval==1:
                    show=True 
                    utf=randint(1,4)*60
                    ltf=utf-60
                    pIt=True
                else:
                    utf=0
                    ltf=0
                    show=False
                print(ranval)
                print(utf)
            if  show and ltf <=frameN % 180 <utf :
                if pIt:
                    print("Drawn")
                    pIt=False
                dot.draw()
                #sample,timestamp = inlet.pull_sample()
                #data=["*",timestamp]
                #data.extend(sample)
                #writer.writerow(data)
                win.flip()
                

        else:
            if frameN % 180 >=150:  
                dot.draw()
                #sample,timestamp = inlet.pull_sample()
                #data=["-",timestamp]
                #data.extend(sample)
                #writer.writerow(data)                
                #print(randint(1,10))

        #rInt = randint(1,10)

                    
        win.flip()


#Random Flashing



win.close()



