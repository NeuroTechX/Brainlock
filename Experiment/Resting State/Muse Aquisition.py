# -*- coding: utf-8 -*-
"""
Created on Thu Dec 08 21:44:49 2016

@author: BCI
"""
import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server


def eeg handler(unused addr, args, ch1, ch2, ch3, ch4):
	print("EEG u(V) per channel:" , ch1 ch2 ch3 ch4)

	
	
	
if name == "  main  ":
	parser = argparse.ArgumentParser()
	parser.add argument(" --ip", 
						default= "127.0.0.1,
						help= "the ip to listen on")
	parser.add argument("--port",
						type=int,
						default=5000,
						help= "The port to listen on")
	args = parser.parse_args()
	
	dispatcher = dispatcher.Dispatcher()
	dispatcher.map("/Debug", print)
	dispatcher.map("/muse/eeg", eeg_handler, "EEG")