"""
EJERCICIO 5: Recursividad

Escribe una función recursiva que imprima la tabla de multiplicar del n

"""



def imprimir_tabla_multiplicar(n, multiplicador=1):
    if multiplicador <= 10:
        resultado = n * multiplicador
        print(f"{n} x {multiplicador} = {resultado}")
        imprimir_tabla_multiplicar(n, multiplicador + 1)

# Llamamos a la función con el valor inicial
imprimir_tabla_multiplicar(5)  # Puedes cambiar el argumento para n según sea necesario

