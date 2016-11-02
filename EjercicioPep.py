#Programa que recibe un string de ADN y devuelve la mayor secuecia TATA en el
#El programa debe recibir un string, recorrerlo y reconocer cuando hay una secuencia TATA correcta
#Una secuencia correcta de TATA es TAT seguido de A por un multiplo de 3
Secuencia = raw_input("introduzca su secuencia de ADN: ")

def Encontrar_TATA(string):
    CadenaTAT = string.find("TAT")
    if CadenaTAT == -1:
        return "no hay ninguna cadena TATA"
    else:
        Secuencia.split([CadenaTAT - 1])
        PosibleCadena = CadenaTAT[1]
        PosibleCadena = str(PosibleCadena)
