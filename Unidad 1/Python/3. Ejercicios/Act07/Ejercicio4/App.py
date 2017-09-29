from Act07.Ejercicio4.Numero import Numero
#Este ejercicio determina si el número que se le pasa es un número primo y nos muestrael nº de primos introducidos y el total
while True:
    num = int(input("Introduzca un número(0: Salir): "))

    if num == 0:
        break;

    numero = Numero(num);
    if numero.esPrimo():
        print("El numero {} es un número primo.".format(num))
    else:
        print("El numero {} NO es un número primo.".format(num))

print("Total numeros introducidos {}, de los cuales {} son primos".format(Numero.totalNumeros, Numero.cuantosPrimos))