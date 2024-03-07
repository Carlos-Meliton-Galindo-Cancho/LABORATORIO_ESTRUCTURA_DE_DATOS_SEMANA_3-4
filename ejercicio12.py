"""
EJERCICIO 12:  Arreglos y Matrices

Calcula la media de los elementos de una matriz

"""



import numpy as np

# Definir una matriz
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calcular la media de los elementos de la matriz
media = np.mean(matriz)

print("Matriz:")
print(matriz)

print("\nMedia de los elementos de la matriz:", media)
