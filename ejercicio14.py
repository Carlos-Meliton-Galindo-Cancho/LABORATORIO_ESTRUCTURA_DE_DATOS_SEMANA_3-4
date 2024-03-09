"""
EJERCICIO 14:  Arreglos y Matrices

Calcula la media, la mediana y la desviación estándar de los elementos de una matriz

"""


import numpy as np                                                                   # se importa la biblioteca NumPy bajo el alias np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],                                                        # se define una matriz utilizando la función np.array()
                   [7, 8, 9]])

media = np.mean(matriz)                                                              # se calcula la media de los elementos de la matriz utilizando np.mean()

mediana = np.median(matriz)                                                          # se calcula la mediana de los elementos de la matriz utilizando np.median()

desviacion_estandar = np.std(matriz)                                                 # se calcula la desviación estándar de los elementos de la matriz utilizando np.std()

print("Matriz:")
print(matriz)
print("\nMedia de los elementos de la matriz:", media)                               # finalmente se imprimen la matriz y los resultados de los cálculos en la consola
print("Mediana de los elementos de la matriz:", mediana)
print("Desviación estándar de los elementos de la matriz:", desviacion_estandar)



"""
LA IMPRESION FINAL SERÁ: 

Matriz:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Media de los elementos de la matriz: 5.0
Mediana de los elementos de la matriz: 5.0
Desviación estándar de los elementos de la matriz: 2.581988897471611
    
"""