"""
EJERCICIO 1: Recursividad

Escribe una función recursiva que imprima los números pares del 1 al 100

"""


def imprimir_pares(n):                  # se define una función llamada imprimir_pares con el parámetro n
    if n <= 100:                        # esta condicional verifica si n es menor o igual a 100. Si es verdadero la función continúa ejecutándose
        if n % 2 == 0:                  # esta condicional verifica si n es par (es decir si el residuo de dividir n entre 2 es igual a cero)
            print(n)                    # si n es par, imprime n
        imprimir_pares(n + 1)           # si n es impar, se llama recursivamente a la funcion con n incrementado en 1

imprimir_pares(1)



"""
LA IMPRESION FINAL EN LA CONSOLA SERÁ:

2
4 
6 
8 
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100

"""
