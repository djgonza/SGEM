from Act07.Ejercicio4.Numero import Numero
#Este ejercicio determina si el número que se le pasa es un número primo.
num = int (input("Introduzca un número: "))

numero = Numero(num)

if numero.esPrimo():
    print("El numero {} es un número primo.".format(num))
else:
    print("El numero {} NO es un número primo.".format(num))