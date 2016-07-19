# IMPORT STATEMENTS

#from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
#Duplicate of below just in case from psychopy import locale_setup, visual, core, event, logging
from psychopy import visual, core, event, logging
from psychopy.constants import *  # things like STARTED, FINISHED
#import numpy as np  # whole numpy lib is available, prepend 'np.'
#from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import csv
import sys # to get file system encoding
#from pylsl import StreamInlet, resolve_stream

#######  LSL Streaming
print("looking for an EEG stream...")
streams = resolve_stream('type','EEG')

# create a new inlet to read from the stream
inlet = StreamInlet(streams[0])

#####

#print("Found it!")
#####Getting the CSV File ready

#Make sure you are in the correct directory
os.chdir('C:\Users\Sydney\Documents\GitHub\Brainlock')

#IMPORT CUSTOM MODULES
#from Password_Setup import *

#PRE-LOAD STIMS

knownA= range(10)
unknowA= range(10)



##Print for Testing Purposes
#print knownA
#print unknownA



## PASWORD SETUP WILL BE IMPLEMENTED IN FUTURE VERSIONS
#Initial Password Input


#INTRO SCREEN
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )


#DATA ACQUISTION LOOP

raw_input("enter to start")

arr_data=[]

    
with open('lsl.csv','wb') as f:
    writer = csv.writer(f)
            
    for i in range(len(acrL)):
              
    while True:
        sample,timestamp = inlet.pull_sample()
        data=[timestamp]
        data.extend(sample)
        writer.writerow(data)
            



