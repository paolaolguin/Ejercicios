#Programa de la guia para la pep
print "Este programa muestra el mayor y menor numero de una lista"

#Funcion que transforma un string de numeros a una lista
lista = raw_input("Ingrese numeros separados por espacios ")
lista = lista.split(" ")
print lista

#Funcion que compara cada elemento de la lista con uno fijo
mayor = None
menor = None
for i in lista:
    i = int(i)
    # not mayor <-> mayor == none, pero en este caso el if toma cero como falso y correria la primera iteracion mas veces
    if mayor == None or menor == None:
        mayor = i #Esto hace que el primer elemento sea tanto el mayor como el menor
        menor = i
    elif i > mayor:
        mayor = i
    elif i < menor:
        menor = i

print "el mayor numero es:", mayor
print "el menor numero es:", menor