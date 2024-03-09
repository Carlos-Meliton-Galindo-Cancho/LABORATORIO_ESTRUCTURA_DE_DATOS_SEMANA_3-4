"""
EJERCICIO 12:  Arreglos y Matrices

Calcula la media de los elementos de una matriz

"""


import numpy as np                                         # se importa la biblioteca NumPy bajo el alias np



matriz = np.array([[1, 2, 3],
                   [4, 5, 6],                                # se define una matriz de 3x3 llamada matriz utilizando la función np.array()
                   [7, 8, 9]])


media = np.mean(matriz)                                      # se calcula la media de todos los elementos de la matriz utilizando la función np.mean() (esta función calcula la media aritmética de los elementos de la matriz)

print("Matriz:")
print(matriz)                                                  # se imprime la matriz original matriz utilizando la función print()

print("\nMedia de los elementos de la matriz:", media)



"""
LA IMPRESION FINAL SERÁ: 

Matriz:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Media de los elementos de la matriz: 5.0
    
"""