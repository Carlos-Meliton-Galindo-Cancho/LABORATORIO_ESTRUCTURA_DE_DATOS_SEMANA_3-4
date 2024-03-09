"""
EJERCICIO 2: Recursividad

Escribe una función recursiva que imprima la suma de los números del 1 al n

"""

def suma(n, suma_actual=0):                            # se define una función llamada suma que toma dos parámetros: n y suma_actual (suma_actual tiene un valor predeterminado de 0)
    if n >= 1:                                         # comprueba si el valor de n es mayor o igual a 1
        suma_actual += n                               # si n es mayor que 1 se grega el valor de n a la suma acumulada
        suma(n - 1, suma_actual)                       # y luego se llama recursivamente a la funcion con n disminuido en 1 y con el valor actual del parametro (suma_actual)
    else:
        print("La suma total es:", suma_actual)        # si n < 1 , entonces se imprime el valor de suma_actual
 
suma(10)                                               # se llama a la funcion con n = 10

"""
LA IMPRESION FINAL SERA: 

La suma total es: 55

"""
