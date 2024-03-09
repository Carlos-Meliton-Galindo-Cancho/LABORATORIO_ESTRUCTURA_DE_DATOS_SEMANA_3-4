"""
EJERCICIO 8:  Arreglos y Matrices

Crea una matriz de matrices

"""



import numpy as np                                          # se importa la biblioteca NumPy bajo el alias np

matriz1 = np.array([[1, 2], [3, 4]])                        # se crea una matriz bidimensional utilizando la función np.array()
matriz2 = np.array([[5, 6], [7, 8]])

matriz_de_matrices = np.array([matriz1, matriz2])           # crea una matriz de matrices

print(matriz_de_matrices)                                   #  imprime la matriz de matrices



"""
LA IMPRESION FINAL SERÁ: 

[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
    
"""