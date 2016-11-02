#Funcion que calcula el factorial de los n primeros numeros naturales
#Definicion funcion recursiva
def calculadora_factorial(x):
    if x == 0:
        return 1
    if x < 0:
        return "Los negativos no tienen factorial. Y dice numero natural."
    else:
        return (x*calculadora_factorial(x-1))
#Entradas
n = input("ingrese un numero natural n ")
n = int(n)
i = 1
#Proceso
while i <= n:
    print calculadora_factorial(i)
    i = i + 1