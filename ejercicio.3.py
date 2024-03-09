"""
EJERCICIO 3: Recursividad

Escribe una función recursiva que imprima la pirámide de números del 1 al n

"""



def imprimir_piramide(n, fila=1):                                  # se define una funcion llamada imprimir_piramide que toma dos parámetros: n y fila (el parámetro fila tiene un valor predeterminado de 1)
    if fila <= n:                                                  # comprueba si fila a es menor o igual que n
        imprimir_fila(n, fila)                                     # si fila <= n llama a la función imprimir_fila para imprimir la fila actual de la piramide
        imprimir_piramide(n, fila + 1)                             # y se llama recursivamente a la función imprimir_piramide para imprimir la siguiente fila de la pirámide (se incrementa fila en 1 en cada llamada recursiva)

def imprimir_fila(n, fila):
    espacios = " " * (n - fila)                                    # esta funcion calcula e imprime las filas de la pirámide concatenando los espacios y los números.
    numeros = " ".join(str(i) for i in range(1, fila + 1))
    print(espacios + numeros)

imprimir_piramide(5)                                               # se llama a la funcion con n = 5



"""
LA IMPRESION FINAL SERÁ: 

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

"""



