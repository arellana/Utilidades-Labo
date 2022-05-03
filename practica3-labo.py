import numpy as np
import matplotlib.pyplot as plt
import random

def randNeg(long):
	aux = []
	for l in range(long):
		aux.append(1 if random.random() < 0.5 else -1)
	return np.asarray(aux)

def oscilador(t,A,fase,freq,xo):
	x = A*np.sin(freq*t + fase) + xo
	ruido = np.asarray(randNeg(len(t))*A/30)
	out = x+ruido
	return out

def osciladorAmortiguado(t,A,fase,freq,gamma,xo):
	x = A*np.exp(-gamma*t)*np.cos(freq*t + fase) + xo
	ruido = np.asarray(randNeg(len(t))*A/30)
	out = x+ruido
	return out

k = 27
m = 0.197

xo = 0
A = 1
fase = np.pi/3
freq = np.sqrt(k/m)
gamma = 0.14
print('frecuencia w: ', freq)

tiempo = np.linspace(0,10,1000)
fig,ax = plt.subplots(2,1,sharex = True, sharey = True)
ax[0].plot(tiempo,oscilador(tiempo,A,fase,freq,xo),'o-', markersize = 3, label = 'Oscilador Amonico')
ax[1].plot(tiempo,osciladorAmortiguado(tiempo,A,fase,freq,gamma,xo),'o-', markersize = 3, label='Oscilador Amortiguado')
plt.xlabel('Tiempo(s)')
plt.ylabel('Amplitud')
plt.legend()
plt.show()

guardar = [tiempo,oscilador(tiempo,A,fase,freq,xo)]
guardar2 = [tiempo,osciladorAmortiguado(tiempo,A,fase,freq,gamma,xo)]

#np.savetxt('oscilador.txt', np.transpose(guardar))#, delimiter = ';')
#np.savetxt('osciladorAmortiguado.txt', np.transpose(guardar2))#, delimiter = ';')