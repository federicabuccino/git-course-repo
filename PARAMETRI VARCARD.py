
# coding: utf-8

# In[ ]:

#PARAMETRI VARIABILITA CARDIACA
get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
distanzaRR=np.load('earclipvarcardpanico.npy')
print(distanzaRR)

plt.plot(distanzaRR)

#calcolo della variab card
varcard=[]
for i in range(len(distanzaRR)-1):
    val=np.abs(distanzaRR[i]-distanzaRR[i+1])
    varcard.append(val)
    
print('variazione cardiaca:' ,varcard)

#asse tempo
xval=[]
x=0
for i in distanzaRR:
    x=x+i
    xval.append(x)
    


#media
media=sum(varcard)/len(varcard)
print('media della variabilità cardiaca:', media)

#deviazione standard
lista=[(x-media)**2 for x in varcard]
dd=sum(lista)/len(lista)
dev_std=np.sqrt(dd)
print('deviazione standard: ',dev_std)



#pnn50
numero=[]
for x in varcard:
    if x>50:
        numero.append(x)
    
pnn50=len(numero)/len(varcard)
print('pnn50 :', pnn50)

#r-MSSD
aa=[]
bb=[]
for i in range(len(varcard)-1):
    diff=np.abs(varcard[i]-varcard[i+1])
    aa.append(diff)
    bb=[x**2 for x in aa]
    ff=sum(bb)/(len(bb)-1)
    rMSSD=np.sqrt(ff)
    
print('r-MSSD:', rMSSD)

#media mobile
y=[]
m=0
for i in range(len(varcard)-5):
    m=sum(varcard[i:i+5])
    mediasu5=m/5
    y.append(float(round(mediasu5,2)))
    
        
print('la media mobile è:',y)

