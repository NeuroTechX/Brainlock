from scipy import signal
import csv
import numpy as np
import matplotlib.pyplot as plt
import itertools
import os
#If using Mac and plotting, write this: export LC_ALL=en_US.UTF-8 and export LANG=en_US.UTF-8
#Get the template for the Cross correlation
os.chdir('/home/sydney/Downloads/CrossCorrelationData')

##Correlation of multiple files.
personlist= ["P01","P02","P03","P04"]
typelist= ["Known_1","Known_2","unKnown_1","unKnown_2"]
eegloclist= ["AF3","AF4","AF7","AF8","AFz","C1","C2","C3","C4","C5","C6","CP1","CP2","CP3","CP4","CP5","CPz","Cz","F1","F2",
             "F3","F4","F5","F6","F7","F8","FC1","FC2","FC3","FC4","FC5","FC1","FC2","FC3","FC4","FC5","FC6","FCZ","Fp1","Fp2",
             "Fpz","FT7","FT8","Fz","Iz","O1","O2","Oz","P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","PO3","PO4","PO7",
             "PO8","POz","Pz","T7","T8","TP7","TP8"]

comblist= list(itertools.product(typelist,eegloclist))

for i in comblist:
        ''.join(i)
        
        
print ''.join(comblist[0])

##script to combine all values into the necessary lists


# 1 list of known1
# 1 list of known2
# 1 list of unknown 1
# 1 list of unknown 2

#Script to do cross correlation of all list

def Openfile(person,location,known,dataset):
  with open(str(person)+"/"+str(location)+str(known)+str(dataset)+'.csv', 'rb') as f:
    reader = csv.reader(f)
    data = reader.next()
    for item in data:
	float(item)
  data = np.array(data,dtype=float)


#Do the actual cross correlation

corr1 = np.correlate(Known_1fP02, Known_2fP01, 'full',True)
corr2 = np.correlate(Known_1fP02, Known_2fP02, 'full',True)
corr3 = np.correlate(Known_1fP02, Known_2fP03, 'full',True)
corr4 = np.correlate(Known_1fP02, Known_2fP04, 'full',True)

print len(corr1)

print "Known 1 vs P01 : "+ str(max(corr1))
print "Known 1 vs P02 : "+ str(max(corr2))
print "Known 1 vs P03 : "+ str(max(corr3))
print "Known 1 vs P04 : "+ str(max(corr4))


##fig, (ax_orig, ax_noise, ax_corr) = plt.subplots(3, 1, sharex=True)
##ax_orig.plot(Known_1)
###ax_orig.plot(clock, Known_1[clock], 'ro')
##ax_orig.set_title('Template from P01')
##ax_noise.plot(Known_2)
##ax_noise.set_title('Testing signal')


###Plot the results
#clock = np.arange(0, len(Known_1f), len(Known_1f)/100)
fig, (x_corrk1k2,x_corru1u2,x_corrk1u1, x_corrk2u2 ) = plt.subplots(4, 1, sharex=True)

##ax_corr_kk.plot(corr1)
##ax_corr_kk.plot(clock, corr1[clock], 'ro')
##ax_corr_kk.axhline(0.5, ls=':')
##ax_corr_kk.set_title('Brain lock authentification Known vs Known')

##x_corrk1k2.xcorr(Known_1f, Known_2f, usevlines=True, maxlags=50, normed=True, lw=2)
##x_corrk1k2.grid(True)
##x_corrk1k2.axhline(0, color='black', lw=2)
##
##x_corru1u2.xcorr(unKnown_1f, unKnown_2f, usevlines=True, maxlags=50, normed=True, lw=2)
##x_corru1u2.grid(True)
##x_corru1u2.axhline(0, color='black', lw=2)
##
##x_corrk1u1.xcorr(unKnown_1f,Known_1f , usevlines=True, maxlags=50, normed=True, lw=2)
##x_corrk1u1.grid(True)
##x_corrk1u1.axhline(0, color='black', lw=2)
##
##x_corrk2u2.xcorr(unKnown_2f, Known_2f, usevlines=True, maxlags=50, normed=True, lw=2)
##x_corrk2u2.grid(True)
##x_corrk2u2.axhline(0, color='black', lw=2)


##ax_corr_ku.plot(corr2)
##ax_corr_ku.plot(clock, corr2[clock], 'ro')
##ax_corr_ku.axhline(0.5, ls=':')
##ax_corr_ku.set_title('Brain lock authentification Known vs unKnown')

fig.tight_layout()
fig.show()
raw_input("Press to close")
