"""
EJERCICIO 16:  Arreglos y Matrices

Escribe una función que encuentre la submatriz de mayor suma de una matriz

"""


import numpy as np                                           # se importa la biblioteca NumPy bajo el alias np

def submatriz_mayor_suma(matriz):                             # definimos la función submatriz_mayor_suma que toma una matriz como entrada
    max_suma = float('-inf')                                 # Inicializamos la suma máxima con un valor muy pequeño
    max_submatriz = None                                    # Inicializamos la submatriz de mayor suma como None

    filas, columnas = matriz.shape                           # se obtienen las dimensiones de la matriz de entrada, es decir, el número de filas y columnas

    
    for i in range(filas):
        for j in range(columnas):                               # se implementa el algoritmo de la suma de submatrices máximo utilizando cuatro bucles anidados
            for k in range(i, filas):                           # estos bucles recorren todas las posibles submatrices dentro de la matriz dada
                for l in range(j, columnas):                    
                    submatriz = matriz[i:k+1, j:l+1] 
                    suma_actual = np.sum(submatriz)                # para cada submatriz se calcula la suma de todos sus elementos utilizando la función np.sum()
                    if suma_actual > max_suma:                     # si la suma actual de la submatriz es mayor que la suma máxima encontrada hasta el momento 
                        max_suma = suma_actual                     
                        max_submatriz = submatriz                  # se actualiza la suma máxima y se guarda la submatriz correspondiente

    return max_submatriz                                           # la función devuelve la submatriz de mayor suma encontrada


matriz_ejemplo = np.array([[1, 2, -1],
                            [-4, 5, 6],                            # se define una matriz de ejemplo matriz_ejemplo para probar la función
                            [7, -8, 9]])


submatriz = submatriz_mayor_suma(matriz_ejemplo)                     # se llama a la función submatriz_mayor_suma() con la matriz de ejemplo


print("Submatriz de mayor suma:")
print(submatriz)                                                # Imprimir la submatriz de mayor suma



"""
LA IMPRESION FINAL SERÁ: 

Submatriz de mayor suma:
[[ 1  2 -1]
 [-4  5  6]
 [ 7 -8  9]]
    
"""
