#Programa que saca el promedio de una lista de numeros

#Entradas
lista = raw_input("inserte numeros separados por espacios ")
lista = lista.split(" ")
suma = 0

#Proceso
for i in lista:
    i = float(i)
    suma = suma + i

Promedio = float(suma/len(lista))
print "El promedio es: ",Promedio