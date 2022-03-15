from io import StringIO
import numpy as np
import matplotlib.pyplot as plt
import os
  
  
# current working directory
# path = os.getcwd()
# print("Current Directory:", path)
  
# parent directory
# parent = os.path.join(path, os.pardir)
  
# prints parent directory
# print("\nParent Directory:", os.path.abspath(parent))



#leo el archivo de datos"
q = open(parent+'/Mediciones/Conductor1.txt').read().replace(',', '.') #Remplazo , por .
p = np.loadtxt(StringIO(q), skiprows=2, delimiter = None) #Tomo solo lo que necesito


#Tomo la columna de voltajes
x_1 = p[:,2]
#print(x_1)


#split_list corta la lista en tantos items segun la discretizacion.
#Para x = 1, despues para x = 3, etc
def split_list(a_list): 
    half = int(len(a_list)/10)  #half es la long total dividido 10
    B = a_list[:half]           #B son los items hasta el valor "half"
    C = a_list[half:]           #C todo lo que sobra
    return B, C                 #lo que me devuelve

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

#print(B,C,D,E,F,G,H,I,J,K)
############################

matris = np.zeros((11,0)) 

#Reconstruyo la columna de voltajes en una matriz
Volt = np.c_[matris, B,C,D,E,F,G,H,I,J,K] #Columnas en X, filas en Y
#print(Volt)
#guardo la matriz
np.savetxt(parent+'/Potenciales/Potencial1.txt', Volt, delimiter = ',')

#aproximo el campo mediante diferencias finitas
Ex = np.zeros((9,8))

for i in range (1,10):
    for j in range (1,9):
        Ex[i-1,j-1] = -(1/2) * (Volt[i-1,j] - Volt[i+1,j])

Ey = np.zeros((9,8))

for i in range (1,10):
    for j in range (1,9):
        Ey[i-1,j-1] = -(1/4) * (Volt[i,j-1] - Volt[i,j+1])

#print(Ex)

#Guardo cada campo        
np.savetxt(parent+'/CamposDiscret/Ex1.txt', Ex, delimiter = ',')
np.savetxt(parent+'/CamposDiscret/Ey1.txt', Ey, delimiter = ',')

#X, Y = np.mgrid[0:8, 0:8] #No hace falta usar el mesh, prque Ex e Ey son de misma dimension
#plt.axes([0.025, 0.025, 0.95, 0.95])
#plt.quiver(Ey, Ex)

#grafico vectorialmente
plt.quiver(Ey, Ex, edgecolor='k', facecolor='teal', linewidth=.5)


Sy = np.zeros((1,10))
Sx = np.zeros((1,10))

for i in range(1,10):
    Sy[:,i] = (8.5/10) * i
    Sx[:,i] = (8/10) * i

Sy = Sy[0,:]
Sx = Sx[0,:]
#print(Sy)

plt.xlim(-0.7, 7.3)
plt.xticks(Sx)
plt.ylim(-0.6,8.5)
plt.yticks(Sy)

plt.savefig(parent+'/CamposPlot/Campo1.png')
plt.show()
