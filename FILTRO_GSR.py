
# coding: utf-8

# In[ ]:

#FILTRO GSR

import numpy as np
snf=np.load("gsrtranqOK.npy")

get_ipython().magic('matplotlib inline')
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal


plt.plot(snf)
plt.title('Segnale originale')
#plt.xlim(0, 1000)
plt.show()

# generazione filtro Fir
time=4
sampleFreq=len(snf)/time
nyqfreq=sampleFreq/2
taglioHz=5
N=83

nsamp=len(snf)
taps=signal.firwin(N, cutoff=taglioHz/nyqfreq)

filtrato=signal.filtfilt(taps,1.0,snf)

plt.figure(1)
plt.plot(taps, 'bo-',linewidth=2)
plt.title('Coefficienti filtro (%d taps)' % N)
plt.show()

#plot risposta in frequenza del filtro FIR
plt.figure(2)
w,h=signal.freqz(taps, worN=8000)
plt.plot((w/np.pi)*nyqfreq, np.absolute(h), linewidth=2)
plt.xlabel('Frequenza(Hz)')
plt.ylabel('Guadagno')
plt.title('Risposta in frequenza del filtro')
plt.ylim(-0.05, 1.05)
plt.grid(True)



plt.figure(3)
#plt.plot(snf)
#plt.ylim(0, 100)
#plt.xlim(10, 340)
plt.plot(filtrato, 'r-')
plt.show()


print(len(snf))


