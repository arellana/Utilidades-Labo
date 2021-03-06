import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from numpy.fft import fft, fftfreq

#En caso de que la tira de datos este cargada con puntuacion para float ","
q = open('data.txt').read().replace(',', '.') #Remplazo , por .
datAAv = np.loadtxt(StringIO(q), delimiter = None)#, skiprows = 2) #Tomo solo lo que necesito

tiempo = datAAv[:,0]
temp = datAAv[:,1]
# Temsmooth = datAAv[:,2]

# for i in range(0,len(tiempo)):
#     tiempo[i] = tiempo[i]/(10**(18))
#     temp[i] = temp[i]/(10**(18))
#     Temsmooth[i] = Temsmooth[i]/(10**(18))

# datos = np.zeros(len(temp))
# for i in range(0,len(temp)):
#     datos[i] = temp[i] - Temsmooth[i]
#     #print(datos6[i], Tsmooth[i])

datos = temp

#Transformada de Fourier
FFT = fft(datos)/len(datos)
real = np.zeros(len(FFT))
imaginario = np.zeros(len(FFT))
for i in range(0,len(FFT)):
    real[i] = FFT.real[i]**2
    imaginario[i] = FFT.imag[i]**2

amplitudFFT = np.zeros(len(FFT))    
for i in range(0,len(FFT)):
    amplitudFFT[i] = real[i] + imaginario[i]
    
print(amplitudFFT)


freq = fftfreq(FFT.size)

# """freq2"""

# freq2 = 1/600

# n = len(datos)
# k = np.arange(n)
# #T = n/




plt.plot(freq, amplitudFFT, 'or')
#plt.plot(tiempo, datos,'o')
plt.show()
