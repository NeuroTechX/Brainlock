# P300 Target Stimuli

This is an explanation of the protocol used for the N400 based EEG biometric authentication system. In this design we flash different acronyms to the user with the expectation that they will known some and depending on the person. This acts as their password. 

##Requirements: 
- Python 2.7+ (https://www.python.org/)
- Psychopy (http://www.psychopy.org/)
- Python OpenBCI (https://github.com/OpenBCI/OpenBCI_Python)
- OpenBCI
- A EEg cap or something to keep the electrodes from not moving.

## Protocol 

This Biometric protocol has not been tested but is currently being used for visualization purposes. This design was inspired by the one used in this study( http://www.ncbi.nlm.nih.gov/pubmed/19163618). It works with one electrode at Cz, with the ground being placed on the forehead and reference on the left earlobe. 



### Data Aquisition

There is a single script right now. No form of feature extraction and classification is done, but will be added in future versions. 


