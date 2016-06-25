# Brainlock
N400 based EEG biometric authentication system

Requirements: 
- Python 2.7+ (https://www.python.org/)
-Python OpenBCI (https://github.com/OpenBCI/OpenBCI_Python)
- Psychopy (http://www.psychopy.org/)

This project has two components - the data collection interface (Experiment) and the implementation of the brainlock (Lock). 

The Experiment phase will allow you to record you brain response to the presented words, and train a classifier to identify your specific brain response. The Lock component will allow you to test your new biometric signature. 

Currently Unimplemented Features: 
Password_Setup.py is called on by WordPresentation_Training.py, and allows you to choose a specifc acronym as your target password, but is currently unimplemented. 
