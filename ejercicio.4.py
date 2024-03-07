"""
EJERCICIO 4: Recursividad

Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n

"""



def imprimir_piramide_invertida(n):
    imprimir_piramide(n, n)

def imprimir_piramide(n, fila):
    if fila >= 1:
        imprimir_fila(n, fila)
        imprimir_piramide(n, fila - 1)

def imprimir_fila(n, fila):
    espacios = " " * (n - fila)
    numeros = " ".join(str(i) for i in range(1, fila + 1))
    print(espacios + numeros)

# Llamamos a la función con el valor inicial
imprimir_piramide_invertida(5)  # Puedes cambiar el argumento para n según sea necesario
