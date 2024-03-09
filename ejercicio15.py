"""
EJERCICIO 15:  Arreglos y Matrices

Escribe una función que encuentre el elemento máximo de una matriz

"""
 
import numpy as np                                            # se importa la biblioteca NumPy bajo el alias np


def encontrar_elemento_maximo(matriz):                        # definimos una función llamada encontrar_elemento_maximo que toma una matriz como argumento
    
    elemento_maximo = np.max(matriz)                          # dentro de la función usamos la función np.max() para encontrar el elemento máximo de la matriz
    return elemento_maximo


matriz_ejemplo = np.array([[1, 2, 3],                          # se define una matriz de ejemplo llamada matriz_ejemplo utilizando la función np.array()
                           [4, 9, 6],                          
                           [7, 8, 5]])


maximo = encontrar_elemento_maximo(matriz_ejemplo)                # llamamos a esta función con una matriz de ejemplo matriz_ejemplo


print("Elemento máximo de la matriz:", maximo)                   # imprimimos el elemento máximo encontrado en la matriz



"""
LA IMPRESION FINAL SERÁ: 

Elemento máximo de la matriz: 9
    
"""
