numOne = float(input("Ingrese un numero: "))
numTwo = float(input("Ingrese otro numero: "))

if numOne == numTwo:
    print("Todos los numeros son solucion")
elif numOne == 0:
    print("No tiene solucion");
else:
    print ("El resultado es {}".format(-numTwo / numOne))