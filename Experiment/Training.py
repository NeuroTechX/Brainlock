# IMPORT STATEMENTS

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import csv
import sys # to get file system encoding
from pylsl import StreamInlet, resolve_stream

#######  LSL Streaming
print("looking for an EEG stream...")
streams = resolve_stream('type','EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

#####


#####Getting the CSV File ready

#Make sure you are in the correct directory
os.chdir('/home/sydney/Brainlock')

#IMPORT CUSTOM MODULES
#from Password_Setup import *

#PRE-LOAD STIMS

knownA= range(10)
unknowA= range(10)


with open('acr.csv','r') as acr:

    reader=csv.reader(acr)
    knownA = reader.next()
    unknownA= reader.next()



##Print for Testing Purposes
#print knownA
#print unknownA

acrL=range(len(knownA))    


#Create the List of Acronyms with known and Unknown
for i in range(len(knownA)):
    if i % 2 == 0:
        acrL[i]=knownA[i]
    else:
        acrL[i]=unknownA[i]



#Change this value if you would like to determine the number of Acronyms you want to use. Makes sure it is a multiple of 2. 
lSize=10

if lSize is not 0:
    acrL=acrL[:lSize]
    print acrL
    print len(acrL)


##### Create a CSV with the person's name. This is the person's ID until we determine
    # how to do all the processing in python
usern = raw_input("Enter your username:")
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

sync = visual.ShapeStim(win, units='', lineWidth=1.5, lineColor='white', 
    lineColorSpace='rgb', fillColor='white', fillColorSpace='rgb', 
    vertices=((0.8, 0.9), (0.9, 0.9), (0.9, 0.8), (0.8,0.8)),
    closeShape=True, pos=(0, 0), size=1, ori=0.0, opacity=1.0, 
    contrast=1.0, depth=0, interpolate=True, name=None, 
    autoLog=None, autoDraw=False)

#win.flip()

#DATA ACQUISTION LOOP

#raw_input("enter to start")

arr_data=[]

with open(usern+'.csv','wb') as f:
    writer = csv.writer(f)
            
    for i in range(len(acrL)):
        
        word = visual.TextStim(win=win, ori=0, name='word',
        text=acrL[i],font=u'Arial',
        pos=[0, 0], height=0.5, wrapWidth=300,
        color=u'white', colorSpace='rgb', opacity=1,
        depth=0.0)      
       # fd = open('data.csv','a')
       # text = all_text[i % 4]
        for frameN in range(180):

            if 0 <= frameN < 60:	   	
                fixation.draw()
                sample,timestamp = inlet.pull_sample()
                data=["+",timestamp]
                data.extend(sample)
                writer.writerow(data)
            if 60 <= frameN < 180:     
                word.draw()
                sync.draw()
                sample,timestamp = inlet.pull_sample()
                data=[acrL[i],timestamp]
                data.extend(sample)
                writer.writerow(data)
           # if 180 <= frameN < 240: 
           #     fixation.draw()
           #     sample,timestamp = inlet.pull_sample()
           #     data=["+",timestamp]
           #     data.extend(sample)
           #     writer.writerow(data)
        
            win.flip()

        

win.close()



