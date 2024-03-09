"""
EJERCICIO 9:  Arreglos y Matrices

Accede al elemento central de una matriz

"""


import numpy as np                                                   # se importa la biblioteca NumPy bajo el alias np

matriz = np.array([[1, 2, 3],                                        # aqui se crea una matriz bidimensional llamada matriz utilizando la función np.array() (a matriz está formada por tres listas anidadas que representan las filas de la matriz)
                   [4, 5, 6],
                   [7, 8, 9]])

elemento_central = matriz[len(matriz)//2, len(matriz[0])//2]         # esta línea accede al elemento central de la matriz y para calcular las coordenadas del elemento central, se utiliza la longitud de la matriz dividida entre 2
print("Elemento central:", elemento_central)



"""
LA IMPRESION FINAL SERÁ: 

Elemento central: 5
    
"""




