"""
EJERCICIO 5: Recursividad

Escribe una función recursiva que imprima la tabla de multiplicar del n

"""



def imprimir_tabla_multiplicar(n, multiplicador=1):                 # se define una función llamada imprimir_tabla_multiplicar que toma dos parámetros: n y multiplicador (parámetro opcional que por defecto se inicializa en 1) 
    if multiplicador <= 10:                                         # esto asegura que la función solo continúe calculando e imprimiendo la tabla de multiplicar hasta el multiplicador 10
        resultado = n * multiplicador
        print(f"{n} x {multiplicador} = {resultado}")               # imprime el resultado utilizando una f-string para formatear la cadena
        imprimir_tabla_multiplicar(n, multiplicador + 1)            # realiza una llamada recursiva a la función imprimir_tabla_multiplicar, incrementando el valor de multiplicador en 1 en cada llamada

imprimir_tabla_multiplicar(5)                                       # llamamos a la función con el valor de 5


"""
LA IMPRESION FINAL SERÁ: 

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
    
"""