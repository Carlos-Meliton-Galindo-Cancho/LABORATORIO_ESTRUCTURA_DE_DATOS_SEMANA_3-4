"""
EJERCICIO 8:  Arreglos y Matrices

Crea una matriz de matrices

"""



import numpy as np

# Definir dos matrices
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

# Crear una matriz de matrices
matriz_de_matrices = np.array([matriz1, matriz2])

print("Matriz de matrices:")
print(matriz_de_matrices)
