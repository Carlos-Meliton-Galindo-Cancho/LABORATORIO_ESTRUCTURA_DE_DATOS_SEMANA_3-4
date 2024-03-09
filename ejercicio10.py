"""
EJERCICIO 10:  Arreglos y Matrices

Suma dos matrices de diferentes tamaños

"""



import numpy as np                                                  # se importa la biblioteca NumPy bajo el alias np

matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matriz2 = np.array([[7, 8, 9, 10],                                  # aqui se definen dos matrices de diferentes tamaños usando la función np.array() (matriz1 tiene dimensiones 2x3 y matriz2 tiene dimensiones 3x4)
                    [11, 12, 13, 14],
                    [15, 16, 17, 18]])

filas_max = max(matriz1.shape[0], matriz2.shape[0])                 # se calcula el número máximo de filas y columnas entre matriz1 y matriz2
columnas_max = max(matriz1.shape[1], matriz2.shape[1])

resultado = np.zeros((filas_max, columnas_max), dtype=int)          # se crea una matriz de ceros llamada resultado con las dimensiones máximas calculadas anteriormente
resultado[:matriz1.shape[0], :matriz1.shape[1]] += matriz1          # se copian los valores de las matrices matriz1 y matriz2 a la matriz resultado (las porciones de la matriz resultado que corresponden a las matrices matriz1 y matriz2 se llenan con los valores de esas matrices)
resultado[:matriz2.shape[0], :matriz2.shape[1]] += matriz2          

print("Matriz 1:")
print(matriz1) 
print("\nMatriz 2:")                                                # se imprime cada una de las matrices originales
print(matriz2)
print("\nMatriz Sumada:")
print(resultado)



"""
LA IMPRESION FINAL SERÁ: 

Matriz 1:
[[1 2 3]
 [4 5 6]]

Matriz 2:
[[ 7  8  9 10]
 [11 12 13 14]
 [15 16 17 18]]

Matriz Sumada:
[[ 8 10 12 10]
 [15 17 19 14]
 [15 16 17 18]]
    
"""


