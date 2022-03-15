# Moverse un directorio arriba respecto de la ubicacion de este archivo

import os

# directorio actual
path = os.getcwd()
print("Current Directory:", path)
  
# directorio superior
parent = os.path.join(path, os.pardir)
print("\nParent Directory:", os.path.abspath(parent))

#leo el archivo de datos.
q = open(parent+'/data.txt').read().replace(',', '.') #Remplazo , por .
p = np.loadtxt(StringIO(q), skiprows=2, delimiter = None) #Tomo solo lo que necesito
