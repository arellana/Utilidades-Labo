#Este Scrypt toma un archivo txt y devuelve una matriz de numeros para cada iteracion.
#Esta pensado para archivos en formato excel u origin (por celdas)

"""
    En datos.txt se debe remplazar por el nombre del archivo a leer, si se usa la convencion
    si se usa la convencion de coma decimal lo cambia a punto, de no ser necesario
    eliminar .replace(',', '.') o remplazarlo por lo que se necesite.
    La subfuncion skiprow esta pensada para nombres de celdas o unidades en valores, para
    para poder operar sobre el mismo archivo sin modificarlo previamente. Ejemplo, tira importada
    desde Origin
"""

import numpy as np
from io import StringIO
import os
import glob

#Lee todo lo que se llame datos*.txt, ejemplo datos1.txt datos2.txt ...
archivos = sorted(glob.glob('datos*.txt')) #El * significa "lo que sea"

# print(archivos)

# Se puede opererar dentro de la iteracion si es que se realiza lo mismo para todos los archivos
for tira in archivos:

    datos = open(tira).read().replace(',','.')
    datos = np.loadtxt(StringIO(datos), skiprows = 4)

 
    columna1 = datos[:,0]
    columna2 = datos[:,1]
    
    ##### Resto del codigo aqui #####
    
    
    #################################
    
