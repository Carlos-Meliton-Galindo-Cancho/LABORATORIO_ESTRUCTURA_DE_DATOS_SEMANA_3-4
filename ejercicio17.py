"""
EJERCICIO 17:  Arreglos y Matrices

Escribe una función que encuentre la matriz de covarianza de dos matrices

"""


import numpy as np                                                   # se importa la biblioteca NumPy bajo el alias np

def matriz_covarianza(matriz1, matriz2):                             # definimos una función llamada matriz_covarianza que toma dos matrices como entrada
    
    min_filas = min(matriz1.shape[0], matriz2.shape[0])
    min_columnas = min(matriz1.shape[1], matriz2.shape[1])           # se ajustan las matrices para que tengan el mismo número de filas y columnas seleccionando solo las primeras min_filas filas y las primeras min_columnas columnas
    matriz1 = matriz1[:min_filas, :min_columnas]
    matriz2 = matriz2[:min_filas, :min_columnas]

    covarianza = np.cov(matriz1, matriz2)                            # calculamos la matriz de covarianza utilizando la función np.cov() de NumPy que calcula la covarianza entre dos matrices
    return covarianza                                                # devolvemos la matriz de covarianza calculada

matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])                                      # probamos la función con dos matrices de ejemplo
             
matriz2 = np.array([[7, 8, 9],
                    [10, 11, 12]])

mat_covarianza = matriz_covarianza(matriz1, matriz2)                 # Llamar a la función para calcular la matriz de covarianza

print("Matriz de covarianza:")
print(mat_covarianza)                                                # Imprimir la matriz de covarianza



"""
LA IMPRESION FINAL SERÁ: 

Matriz de covarianza:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
    
"""