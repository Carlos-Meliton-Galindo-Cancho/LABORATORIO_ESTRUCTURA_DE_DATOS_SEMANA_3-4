"""
EJERCICIO 11:  Arreglos y Matrices

Multiplica una matriz por un número

"""



import numpy as np                                                 # se importa la biblioteca NumPy bajo el alias np


matriz = np.array([[1, 2, 3],
                   [4, 5, 6],                                      # se define una matriz de 3x3 llamada matriz utilizando la función np.array()
                   [7, 8, 9]])


numero = 2                                                     # se inicializara numero que se utilizará para multiplicar cada elemento de la matriz


matriz_resultante = matriz * numero                              # se multiplica cada elemento de la matriz por el número (numero)

print("Matriz original:")
print(matriz)
 
print("\nMatriz multiplicada por", numero, ":")                 # se proporcionan mensajes descriptivos para indicar qué matriz se está imprimiendo y se muestra el número por el cual se multiplicó la matriz original
print(matriz_resultante)



"""
LA IMPRESION FINAL SERÁ: 

Matriz original:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Matriz multiplicada por 2 :
[[ 2  4  6]
 [ 8 10 12]
 [14 16 18]]
    
"""