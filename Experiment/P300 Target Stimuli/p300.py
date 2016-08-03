# IMPORT STATEMENTS

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from multiprocessing import Process, Queue
from psychopy import locale_setup, visual, core, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from os import listdir
from os.path import isfile, join
import csv
import sys # to get file system encoding
import random
from pylsl import StreamInlet, resolve_stream
###Place the path to where the pictures are below"
path=""
#######  LSL Streaming
#print("looking for an EEG stream...")
#streams = resolve_stream('type','EEG')

# create a new inlet to read from the stream
#inlet = StreamInlet(streams[0])

#print("Found it!")
#####Getting the CSV File ready

#Make sure you are in the correct directory


#PRE-LOAD STIM

#### Images List #######

plist  = [f for f in listdir(path) if isfile(f)]

##### Create a CSV with the person's name. This is the person's ID
usern = raw_input("Enter your username:")
#####



#INTRO SCREEN
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )

#CREATE NONTEXT OBJECTS 


fixation = visual.GratingStim(win=win, mask='cross', size=0.25, pos=[0,0], sf=0.1)

sync = visual.ShapeStim(win, units='', lineWidth=1.5, lineColor='white', 
    lineColorSpace='rgb', fillColor='white', fillColorSpace='rgb', 
    vertices=((0.8, 0.9), (0.9, 0.9), (0.9, 0.8), (0.8,0.8)),
    closeShape=True, pos=(0, 0), size=1, ori=0.0, opacity=1.0, 
    contrast=1.0, depth=0, interpolate=True, name=None, 
    autoLog=None, autoDraw=False)



####Variables For the Loop#####
clock=core.Clock()
###/End of Variables For the Loop#####


def lsl(q):   
    with open(usern+'.csv','wb') as f:
        writer = csv.writer(f)
        power=1
        stim= "+"
        #if not q.empty():
        #   power,stim =q.get() 
            
        while power==1:    
            if q.empty():
                sample,timestamp = inlet.pull_sample()
                data=[stim,timestamp]
                data.extend(sample)
                writer.writerow(data)
            else:
                power,stim =q.get()



###Code Below is all the  Main Loop It assumed that you have a monitor refresh rate#####
###of 60 Hz where each value in the range is 1/60 seconds
if __name__ == "__main__":    
    #q= Queue()
#    q.put([1,"+"])
    #l= Process(target=lsl,args=(q,))
    #l.start()
    for k in range(len(plist)):
        image = visual.ImageStim(win, image=plist[k], mask=None, units='', pos=(0.0, 0.0), size=None, ori=0.0, color=(1.0, 1.0, 1.0)
                   , colorSpace='rgb', contrast=1.0, opacity=1.0, depth=0, interpolate=False, flipHoriz=False
                   , flipVert=False, texRes=128, name=None, autoLog=None, maskParams=None)
        #i=k                      
        for frameN in range(180):
            win.flip()
##            if frameN ==0:
##                q.put([1,"+"])            
            if 0 <= frameN < 60:	   	
##                print("0-60: Time - %f",(clock.getTime()))
                fixation.draw()               
##            if frameN == 60:
##                q.put([1,acrL[k]])
            if 60 <= frameN < 180:
                image.draw()
##                print("60-180: Time - %f",(clock.getTime()))
            
    q.put([0,""])
    l.terminate()            
    win.close()    
               


