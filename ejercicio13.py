"""
EJERCICIO 13:  Arreglos y Matrices

Crea una matriz de números aleatorios de tamaño 100x100

"""


import numpy as np                                          # se importa la biblioteca NumPy bajo el alias np

matriz_aleatoria = np.random.rand(100, 100)                 # se utiliza la función np.random.rand() para generar una matriz de números aleatorios de tamaño 100x100

print("Matriz de números aleatorios:")
print(matriz_aleatoria)                                     # se imprime la matriz resultante en la consola


