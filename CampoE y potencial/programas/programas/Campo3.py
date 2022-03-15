from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import os
  
path = os.getcwd()
parent = os.path.join(path, os.pardir)

q = open(parent+'/Mediciones/Conductor3.txt').read().replace(',', '.') #Remplazo , por .
p = np.loadtxt(StringIO(q), skiprows=2, delimiter = None) #Tomo solo lo que necesito

#print(p)

### Tomo todas las filas iguales

x_1 = p[:,2]
# print(x_1)

def split_list(a_list):
    half = int(len(a_list)/10)
    return a_list[:half], a_list[half:]

B, C = split_list(x_1)


def split_list2(a_list):
    half = int(len(a_list)/9)
    return a_list[:half], a_list[half:]

C, D = split_list2(C)

def split_list3(a_list):
    half = int(len(a_list)/8)
    return a_list[:half], a_list[half:]

D, E = split_list3(D)

def split_list4(a_list):
    half = int(len(a_list)/7)
    return a_list[:half], a_list[half:]

E, F = split_list4(E)

def split_list5(a_list):
    half = int(len(a_list)/6)
    return a_list[:half], a_list[half:]

F, G = split_list5(F)

def split_list6(a_list):
    half = int(len(a_list)/5)
    return a_list[:half], a_list[half:]

G, H = split_list6(G)

def split_list7(a_list):
    half = int(len(a_list)/4)
    return a_list[:half], a_list[half:]

H, I = split_list7(H)

def split_list8(a_list):
    half = int(len(a_list)/3)
    return a_list[:half], a_list[half:]

I, J = split_list8(I)

def split_list9(a_list):
    half = int(len(a_list)/2)
    return a_list[:half], a_list[half:]

J, K = split_list9(J)

############################

matris = np.zeros((11,0)) 

Volt = np.c_[matris, B,C,D,E,F,G,H,I,J,K] #Columnas en X, filas en Y
#print(Volt)
np.savetxt(parent+'/Potenciales/Potencial3.txt', Volt, delimiter = ',')


Ex = np.zeros((9,8))

for i in range (1,10):
    for j in range (1,9):
        Ex[i-1,j-1] = -(1/2) * (Volt[i-1,j] - Volt[i+1,j])

Ey = np.zeros((9,8))

for i in range (1,10):
    for j in range (1,9):
        Ey[i-1,j-1] = -(1/4) * (Volt[i,j-1] - Volt[i,j+1])

#print(Ex)
np.savetxt(parent+'/CamposDiscret/Ex3.txt', Ex, delimiter = ',')
np.savetxt(parent+'/CamposDiscret/Ey3.txt', Ey, delimiter = ',')

#X, Y = np.mgrid[0:10, 0:10] #No hace falta usar el mesh, prque Ex e Ey son de misma dimension



Sy = np.zeros((1,10))
Sx = np.zeros((1,10))

for i in range(1,10):
    Sy[:,i] = (9/10) * i
    Sx[:,i] = (8/10) * i

Sy = Sy[0,:]
Sx = Sx[0,:]
#print(Sy)




plt.quiver(Ey, Ex, edgecolor='k', facecolor='teal', linewidth=.5)


plt.xlim(-0.9, 7.5)
plt.xticks(Sx)
plt.ylim(-0.8,9.1)
plt.yticks(Sy)


plt.savefig(parent+'/CamposPlot/Campo3.png')
plt.show()
