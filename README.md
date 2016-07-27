# Brainlock

Brainlock is a N400 based EEG biometric authentication system. In this design we flash different acronyms to the user with the expectation that they will known some and depending on the person. This acts as their password. 

Depending on the person, you may need to test whether they know the acronym or not (there is a script called acrselection). Run the 

##Requirements: 
- Python 2.7+ (https://www.python.org/)
- Psychopy (http://www.psychopy.org/)
- Python OpenBCI (https://github.com/OpenBCI/OpenBCI_Python)
- Octave (If you prefer, a Matlab script will also be provided)  
- EEGLab (https://sccn.ucsd.edu/eeglab)
- an OpenBCI
- A EEg cap or something to keep the electrodes from not moving.
- 

## Protocol 

protocol has 3 steps that are associated with it:

1) Data Aquisition (Using Psychopy and OpenBCI)
2) Biometric Template (Using EEGLab and Octave)
3) Testing 



### Data Aquisition

This project is really early in its development and as such, you will need to run multiple scripts 

To build the eeg For the Aquisition Script of the eeg template , 

For the OpenBCI, you will need to have your pins configured properly. Depending on the person, the suggested amount of electrodes to work with would be around 5: 3 would be your points of eeg aquisition, 1 would be your reference and 1 would be your ground. 

### Signal Processing and Classification

In order to do this, all that is required is to run octave with EEGlab. Once the script is complete, you should be able to take your csv then run the BrainLock script


### Testing

In order to dertmine if you have a good EEG template, you can run the Brainlock script. You can select if you want to do a live or csv test, where you compare an eeg session with the template. This will inform you how good your reading is.

# TODO:

* Improving Robustness is critical to make this something liable to be used in the field. Whether it is expanding for it to use other hardware or improve the signal processing and classification, This should be improved first before anything else. 
* Update scripts to match the style conventions of Pythno

