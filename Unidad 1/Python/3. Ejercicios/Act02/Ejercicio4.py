print("Comparador de numeros")
numOne = int(input("Escriba un numero: "))
numTwo = int(input("Escriba otro: "))

if numOne > numTwo:
    if numOne % numTwo == 0:
        print("{} es multiplo de {}".format(numOne, numTwo))
    else:
        print("{} no es multiplo de {}".format(numOne, numTwo))
else:
    if numTwo % numOne == 0:
        print("{} es multiplo de {}".format(numTwo, numOne))
    else:
        print("{} no es multiplo de {}".format(numTwo, numOne))