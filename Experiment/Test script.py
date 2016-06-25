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
from Password_Setup import *

#PRE-LOAD STIMS
Random_Words = ["mit","skt","tag","ttl","bul","uno","dye","rep","bit","urd","rev","hkj","gov","key","fil","mic","mfr","vic",
    "due","tow","yam","kum","boa","dix","sqq","sax","bar","din","ajo","mid","rco","esr","psv","bub","ode","ely","fid","buy",
    "eeg","tiu","wad","hot","hrh","per","hay","abb","caf","twp","mir","aft","dbh","run","gie","jud","syr","wey","whr","dpt",
    "ufa","era","mch","tob","moi","wry","oat","dfm","zoe","dmz","bim","dew","hyp","eta","woo","wpc","exp","avo","bpc","lsd",
    "alp","dag","tub","yet","axa","aso","bag","rah","pep","brl","rnr","ctv","ton","fet","yak","pit","cut","coy","anu","mfg",
    "rel","don"]

##Test data is here just to manage experiment
random_Test=["mit","skt","tag"]

## PASWORD SETUP WILL BE IMPLEMENTED IN FUTURE VERSIONS
#Initial Password Input
#passfinal = 'hi' #passwordsetup()

#INTRO SCREEN
win = visual.Window(size=(1000, 1000), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

fixation.draw()

win.flip()

#all_text = [Password,Random_0,Random_1,Random_2]

#DATA ACQUISTION LOOP

#raw_input("enter to start")

arr_data=[]

with open('data3.csv','wb') as f:
    writer = csv.writer(f)
            
    for i in range(3):
        
        word = visual.TextStim(win=win, ori=0, name='word',
        text=random_Test[i],font=u'Arial',
        pos=[0, 0], height=0.5, wrapWidth=300,
        color=u'white', colorSpace='rgb', opacity=1,
        depth=0.0)      
       # fd = open('data.csv','a')
       # text = all_text[i % 4]
        for frameN in range(200):

            if 0 <= frameN < 50:	   	
                fixation.draw()
                sample,timestamp = inlet.pull_sample()
                data=["+",timestamp]
                data.extend(sample)
                writer.writerow(data)
            if 50 <= frameN < 150:     
                word.draw()
                sync.draw()
                sample,timestamp = inlet.pull_sample()
                data=[random_Test[i],timestamp]
                data.extend(sample)
                writer.writerow(data)
            if 150 <= frameN < 200: 
                fixation.draw()
                sample,timestamp = inlet.pull_sample()
                data=["+",timestamp]
                data.extend(sample)
                writer.writerow(data)
        
            win.flip()

        

win.close()



