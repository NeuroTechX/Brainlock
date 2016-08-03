# N400 Acronyms

This is an explanation of the protocol used for the N400 based EEG biometric authentication system. In this design we flash different acronyms to the user with the expectation that they will known some and depending on the person. This acts as their password. 


##Requirements: 

- Python 2.7+ (https://www.python.org/)
- Psychopy (http://www.psychopy.org/)
- Python OpenBCI (https://github.com/OpenBCI/OpenBCI_Python)
- Matlab (To be converted in Octave)
- EEGLab (https://sccn.ucsd.edu/eeglab)
- an OpenBCI
- A EEg cap or something to keep the electrodes from not moving.


## Protocol 
 
### Participants 
Use healthy people with no neurological abnormalities (epilepsy, multiple sclerosis…). Know that the response will inevitably vary from person to person because what can be read on scalp electrodes is subject to how the participant’s brain folds (sulci and gyri), skull thickness and general neuroanatomy. This gives rise to very broad individual differences (Homan, R. W., Herman, J., & Purdy, P. (1987). Cerebral location of international 10–20 system electrode placement. Electroencephalography and clinical neurophysiology, 66(4), 376-382.).

### Stimuli
Here we used known acronyms mixed with false words/unknown acronyms. Participants first identified what words were known and what words were unknown to them. Now, if the person does not specifically know what the word means, BUT has a feeling of knowing the word, classify it as known.

### Procedure
Be sure that the participant is fully informed of what is going to happen beforehand. Know that the procedure we implemented is an oversimplied version of this paper (Laszlo, S., & Federmeier, K. D. (2007). Better the DVL you know acronyms reveal the contribution of familiarity to single-word reading. Psychological Science, 18(2), 122–126.). Participants first were informed what we were going to do, electrodes were fitted to their head using conductive gel and a cap. We performed the test with RESEARCH EQUIPMENT (see the Data Acquisition section). We also tested this with Python and OpenBCI, with no avail. Basically, you should know that the ERP approach was designed specifically for research purposes and it is actually a bit tricky to get it outside of research environments. Our suggestion to you is that, if you are going to try something you saw in published scientific literature, stick to the scientific experimental protocol as much as you can (we simplified a one hour experiment into a 10 minute one). 

### Data acquisition: 
We performed the experiment in two different environments: open science equipment (OpenBCI, Python, Florida Research Instruments), and with research equipment (Biosemi, MATLAB). 
#### Open BCI
 We were not able to get a clean enough signal with OpenBCI. We tried it with two type of electrodes: Ag-AgCl (Florida Research Instruments; dry electrodes) and Au (OpenBCI; we exfoliated the scalp skin with NuPrep to clean the scalp and then attached the electrodes to the scalp using conductive paste ten20). The scripts used for this experimental approach are found in the current folder. We connected OpenBCI to a Mac (though we ran with a LOT of issues regarding PsychoPy and its dependencies) and it was also done with Ubuntu. The participant sat down in a quiet environment with lights off, sat about a meter away from the computer monitor and the experiment started. Csv files were recollected and analyzed using MATLAB. 

For this design, it only required hypothetically the O2 location with a ground on the forehead and earlobe as the reference.

####Research environment
We used 64Ag-AGCl electrodes placed on the scalp according to the international 10/10 system (ActiveTwo, Biosemi) + 6 external electrodes (Nose, Horizontal Electrooculogram Left, Horizontal Electrooculogram Right, Vertical Electrooculogram, Nose, Left Mastoid, Right Mastoid). This system records the data without a reference (http://www.biosemi.com/faq/cms&drl.htm). We used a sampling rate of 2048 Hz and performed the experiment in an electromagnetically and acoustically isolated room. We presented the data using MATLAB (an old version of the data acquisition toolbox and psychtoolbox). Though our data was clean for some participants, the amount of acronyms used was clearly not enough. Also, Psychtoolbox is known to have jitter issues, to which ERPs are very sensitive (introducing nuisance time variations that will mess up the final averaging process). 


###Signal Processing:
 Signal were analyzed in two ways: Open using MATLAB’s EEGLAB toolbox (https://sccn.ucsd.edu/eeglab/). The scripts can be found in the matlab folder
####CSV files created with OpenBCI and Python:
Still working on the documentation. Will be added soon.

#### Bdf files created with the Biosemi setup
 The BDF files were imported using the pop_reabdf function. After that, we deleted unused channels (namely the 6 external electrodes) using pop_select function. Signal was then re-referenced to common average reference (because Biosemi records signal without a reference, we need to do this step in the very early processing stage) using the pop_reref function. We then assign channel locations using standard Besa files (pop_chaedit), we filter from 1 - 40 Hz (pop_basicfilter) and save the EEG structure. From this, we do two different processing procedures: one that plots the ERPs and one that creates the csv files to feed into the Python cross-correlation 



