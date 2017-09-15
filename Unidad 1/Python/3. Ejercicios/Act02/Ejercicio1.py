print("Divisor de números")
numOne = int(input("Escriba el dividendo: "))
numTwo = int(input("Escriba el divisor: "))
cociente = int(numOne / numTwo)
resto = numOne % numTwo
if resto ==0:
    print("La división es exacta. Cociente: {}".format(cociente))
else:
    print("La división NO es exacta. Cociente: {} Resto: {}".format(cociente, resto))