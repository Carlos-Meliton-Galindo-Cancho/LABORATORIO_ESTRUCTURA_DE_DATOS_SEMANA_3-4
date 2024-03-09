"""
EJERCICIO 4: Recursividad

Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n

"""



def imprimir_piramide_invertida(n):                        # se define una función llamada imprimir_piramide_invertida que toma un parámetro n
    imprimir_piramide(n, n)                                # llama a la función imprimir_piramide con los parámetros n y n (n se pasa dos veces ya que representa tanto el número máximo de filas como la fila actual que se está imprimiendo en la pirámide)

def imprimir_piramide(n, fila):
    if fila >= 1:                                            # verifica si el valor de fila es mayor o igual a 1
        imprimir_fila(n, fila)                               # llama a la función imprimir_fila con los parámetros n y fila para imprimir la fila actual de la pirámide
        imprimir_piramide(n, fila - 1)                        #  llamada recursiva a la función imprimir_piramide con los mismos parámetros n, y fila - 1 (esto asegura que la función continúe imprimiendo las filas restantes de la pirámide)

def imprimir_fila(n, fila):
    espacios = " " * (n - fila)                                  # calcula la cantidad de espacios necesarios antes de imprimir los números en la fila actual
    numeros = " ".join(str(i) for i in range(1, fila + 1))        # genera una cadena de números separados por un espacio, comenzando desde 1 hasta el valor de fila
    print(espacios + numeros)


imprimir_piramide_invertida(5)                       # # llamamos a la función con el valor de 5



"""
LA IMPRESION FINAL SERÁ: 

1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
    
"""








