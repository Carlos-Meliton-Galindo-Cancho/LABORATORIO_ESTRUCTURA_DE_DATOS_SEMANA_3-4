"""
EJERCICIO 9:  Arreglos y Matrices

Accede al elemento central de una matriz

"""

# Número impar de filas y columnas:


import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Acceder al elemento central
elemento_central = matriz[len(matriz)//2, len(matriz[0])//2]
print("Elemento central:", elemento_central)






