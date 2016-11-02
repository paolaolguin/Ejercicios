def encontranding_numeromayor(x):
    positivos = []
    negativos = []
    ceros = []
    for element in x:
        if element > 0:
            positivos.append(element)
        elif element == 0:
            ceros.append(element)
        else:
            negativos.append(element)
    if len(positivos) != 0:
        a = 0
        i = 0
        while i < len(positivos):
            if a < positivos[i]:
                a = positivos[i]
            i = i + 1
        return a
    if len(positivos) == 0:
        if len(ceros) != 0:
            a = 0
            return a
    if len(positivos) == 0:
        if len(ceros) == 0:
            if len(negativos) != 0:
                b = len(negativos)
                j = 0
                nuevos_negativos = []
                while j < b:
                    a = 0
                    for i in negativos:
                        if a > i:
                            a = i
                    nuevos_negativos.append(a)
                    negativos.remove(a)
                    j = j + 1
                b = len(nuevos_negativos)
                a = nuevos_negativos[b - 1]
                return a


# Entrada
numeros = input("Ingrese la lista a analizar")
# Procesamiento
i = 0
j = len(numeros)
nuevos_numeros = []
while i < j:
    numero_nuevo = encontranding_numeromayor(numeros)
    nuevos_numeros.append(numero_nuevo)
    numeros.remove(numero_nuevo)
    i = i + 1
# Salida
print "La lista con los numeros ordenados de mayor a menor es: ", nuevos_numeros

