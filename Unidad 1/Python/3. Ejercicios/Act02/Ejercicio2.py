print("Comparador de numeros")
numOne = int(input("Escriba un numero: "))
numTwo = int(input("Escriba otro: "))

if numOne > numTwo :
    print ("{} es mayor que {}".format(numOne, numTwo))
elif numOne < numTwo:
    print ("{1} es mayor que {0}".format(numOne, numTwo))
else:
    print ("Los numeros son iguales")
