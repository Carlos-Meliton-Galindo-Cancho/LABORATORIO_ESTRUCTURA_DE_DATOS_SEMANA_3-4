"""
EJERCICIO 10:  Arreglos y Matrices

Suma dos matrices de diferentes tamaños

"""



import numpy as np

# Definir dos matrices de diferentes tamaños
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matriz2 = np.array([[7, 8, 9, 10],
                    [11, 12, 13, 14],
                    [15, 16, 17, 18]])

# Crear una matriz resultante con la dimensión más grande
filas_max = max(matriz1.shape[0], matriz2.shape[0])
columnas_max = max(matriz1.shape[1], matriz2.shape[1])

# Inicializar matrices con ceros y copiar valores
resultado = np.zeros((filas_max, columnas_max), dtype=int)
resultado[:matriz1.shape[0], :matriz1.shape[1]] += matriz1
resultado[:matriz2.shape[0], :matriz2.shape[1]] += matriz2

print("Matriz 1:")
print(matriz1)
print("\nMatriz 2:")
print(matriz2)
print("\nMatriz Sumada:")
print(resultado)
