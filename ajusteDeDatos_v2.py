"""Esta es la version basica para ajustar funciones, algo tediosa ya que hay que cambiar el scrypt
   para cada vez que se quiera cambiar la funcion a ajustar como la tira de datos; posteriormente
   se va a cambiar esto para poder trabajar desde entradas en la terminal del sistema o desde una
   ventana emergente. 

   Los archivos 'datos.txt' y 'datosAux.txt' deben estar en el mismo directorio donde se encuentra
   este scrypt""" 

"""Actualizacion 1/2/18: Se agregó el calculo del valor de R-square, este puede obtenerse
   de dos formas distintas segun como se desatalla en el correspondiente bloque"""

#Importo librerias que voy a usar:
import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

#Cargo los datos (cambiar el nombre del archivo segun el .txt)
p = np.loadtxt('datos.txt', usecols=(0, 1) , skiprows=1, delimiter = None).astype(int)

#Archivo auxiliar para otras mediciones
e = np.loadtxt('datosAux.txt', skiprows=1, delimiter = None)

#Armo las tiras de datos (cambiar segun la posicion de las columnas) (Recordar que el indexado empieza en 0)
Columna1 = p[:, 0]
Columna2 = p[:, 1]

ColumnaAux1 = e[:, 2]
ColumnaAux2 = e[:, 3]

#Defino la funcion a fitear (x: variable; a,b: parametros, agregar mas de ser necesario)
def f(x, a, b):
    #Funcion por la cual ajusto
    return a * (x ** b)    

#valor de parametros y sus desviacion standar (ver documentacion de scipy para conocer la aproximacion)    
(a, b), c= curve_fit(f, Columna1, Columna2)
print(a, b)

#rango en el que se mueven los datos
x = np.linspace(550, 1000)




########R-square########

"""El calculo del 'Coeficiente de determinacion', se realiza mediante la
ecuacion definida como:

R² := 1 - (SS_res / SS_tot)

donde SS_res es la suma de los cuadrados de las diferencias entre los valor
obtenidos y los valores teoricos. SS_tot es analogo, variando en que la
diferencia es entre el valor medido y el promedio de todos los valores.

Este esta pensado para utilizar en la segunda columna los valores del eje Y
y en la primera la de el eje X, de no estar ordenados asi, es necesario editar
las variables"""

n = len(Columna2)
Yprom = (1/n) * np.sum(Columna2)

Ydif1sq = np.zeros(n)
for i in range(0,n):
    Ydif1sq[i] = (Columna2[i] - Yprom)**2

SS_tot = np.sum(Ydif1sq)

Ydif2sq = np.zeros(n)
fun = f(Columna1,a,b)  #fun va a depender de los paramatros calculados, agregar tantos como sean necesarios
for i in range(0,n):
    Ydif2sq[i] = (fun[i] - Yprom)**2

SS_reg = np.sum(Ydif2sq)

Ydif3sq = np.zeros(n)
for i in range(0,n):
    Ydif3sq[i] = ((Columna2[i]) - (fun[i]))**2

SS_res = np.sum(Ydif3sq)


Rsqr = 1 - (SS_res / SS_tot) #Valor planteado incialmente
Rsqr2 = (SS_reg / SS_tot)    #Valor obtenido mediante el uso de SS_res + Ss_reg = SS_tot

"""Puede que ambos valores difieran segundo las mediciones, cambiar
la siguiente linea en caso de queres que se muestre el otro valor""" 
print('R-square: ', Rsqr)

############Grafico############

#Grafico los datos
plt.plot(Columna1, Columna2, 'ob', )

#grafico el fit
plt.plot(x, f(x, a, b))

#grafico de errores
plt.errorbar(Columna1, Columna2, ColumnaAux1, ColumnaAux2, 'o', ecolor='red')

#Leyendas de ejes
plt.xlabel('Valor de X')
plt.ylabel('Valor de Y')

#guardo el plot
#plt.savefig('Ajuste_picos.png')

#mostrar grafico
plt.show()
