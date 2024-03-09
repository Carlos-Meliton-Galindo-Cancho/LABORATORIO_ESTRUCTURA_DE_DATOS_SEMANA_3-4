"""
EJERCICIO 7:  Arreglos y Matrices

Crea una matriz de números complejos

"""



import numpy as np                                                    # se importa la biblioteca NumPy bajo el alias np

matriz_complejos = np.array([[1 + 2j, 3 - 4j, 5 + 6j],                # se crea una matriz de números reales utilizando la función np.array()
                             [7 - 8j, 9 + 10j, 11 - 12j],
                             [13 + 14j, 15 - 16j, 17 + 18j]])

print(matriz_complejos)                                               #  imprime la matriz de números complejos



"""
LA IMPRESION FINAL SERÁ: 

[[ 1. +2.j  3. -4.j  5. +6.j]
 [ 7. -8.j  9.+10.j 11.-12.j]
 [13.+14.j 15.-16.j 17.+18.j]]
    
"""