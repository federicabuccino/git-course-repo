
# coding: utf-8

# In[ ]:

#ESECUZIONE SENSORI
get_ipython().magic('matplotlib inline')
from pynq.pmods import Grove_ADC
import time
import matplotlib.pyplot as plt
import numpy as np
from pynq.pmods import Grove_EarHR
from pynq.board import LED
from pynq.pmods import PMOD_IO
from IPython import display

#definizione e posizionamento LED (collegamenti ai PMOD)
giallo=PMOD_IO(3,0, 'out')
rosso=PMOD_IO(3,1, 'out')
verde=PMOD_IO(4,0, 'out')


def funzled(x):
    verde.write(x)
    giallo.write(x)
    rosso.write(x)
#inizializzazione LED
funzled(0)

#generazione liste
valorifreq=[]
distRR=[]
valoriGSR=[]

#inizializzazione sensore EarClip sul PMOD 2 (JC) e grove id 4 (GR4)
earHR = Grove_EarHR(2, 4)

# inizializzazione del Led della Zybo
led = LED(0)
led.off()

# lettura valori iniziali battito cardiaco
beats, deltaT = earHR.read_raw()
oldBeats = beats

#definizione e posizionamento ADC sul PMOD 1(JB) e grove id 4(GR4)
grove_adc = Grove_ADC(1, 4)

delta = 60
start = time.time()
end = start

while(end - start < delta):
    valoriGSR.append(grove_adc.read())
    time.sleep(0.05)
    end = time.time()
    try:
        beats, deltaT = earHR.read_raw()
        if(oldBeats == beats):
            # stesso numero di battiti rispetto alla precedente iterazione
            led.off()
        else:
            # battito!
            led.on()
            distRR.append(deltaT)
            
        oldBeats = beats
        rate = earHR.read()
        valorifreq.append(rate)
        
        display.clear_output(wait=True)
        print("Numero di battiti cardiaci: " + str(beats))
        print("Frequenza cardiaca: " + str(round(rate,2)) + " battiti al minuto")
        
        time.sleep(0.05)
        
        if rate>=60 and rate <=90:
            verde.write(1)
            giallo.write(0)
            rosso.write(0)
        if rate<60:
            giallo.write(1)
            verde.write(0)
            rosso.write(0)
        if rate>90:
            rosso.write(1)
            verde.write(0)
            giallo.write(0)
        
    except KeyboardInterrupt:
        # uscita senza mostrare errore se premuto il bottone di stop in Jupyter
        break

        
        
#reset dei led
funzled(0)

delta = end - start
#calcolo variabilità cardiaca
varcard=[]
for i in range(len(distRR)-1):
    val=np.abs(distRR[i]-distRR[i+1])
    varcard.append(val)
    
print('variazione cardiaca:' ,varcard)
print("Tempo di acquisizione: " +str(delta)+ " s")
print("Numero di campioni GSR: "+str(len(valoriGSR))+" campioni")
print("Campionamento GSR: " +str(len(valoriGSR) / delta)+ " Hz")

print("Numero campioni variabilità cardiaca: "+str(len(varcard))+" campioni")
print("Campionamento EarClip: "+str(len(varcard)/delta)+" Hz")




#disegna grafico GSR conduttanza
plt.figure(1)
plt.plot(range(len(valoriGSR)), valoriGSR, 'r')
plt.title('ADC data-conduttanza')
plt.xlabel("Campioni[n]")
plt.ylabel("GSR data")


#disegna grafico variabilità cardiaca
plt.figure(2)
plt.plot(varcard)
plt.xlabel("Campioni[n]")
plt.ylabel("Tempo [ms]")
plt.show()


#disegna grafico distanza RR
plt.figure(3)
plt.plot(distRR)
plt.xlabel("Campioni[n]")
plt.ylabel("Tempo [ms]")
plt.show()
#salvataggio valori

np.save('gsrtranqOK',valoriGSR)
np.save('earcliptranqOK', distRR)

