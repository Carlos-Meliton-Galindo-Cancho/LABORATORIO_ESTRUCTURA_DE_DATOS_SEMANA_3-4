"""
EJERCICIO 11:  Arreglos y Matrices

Multiplica una matriz por un número

"""



import numpy as np

# Definir una matriz
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Definir el número por el cual multiplicar la matriz
numero = 2

# Multiplicar cada elemento de la matriz por el número
matriz_resultante = matriz * numero

print("Matriz original:")
print(matriz)

print("\nMatriz multiplicada por", numero, ":")
print(matriz_resultante)
