import Act05.ej4.functions as func
numOne = input("Inserte numero: ")
numTwo = input("Inserte otro numero: ")

print("Suma {} + {} : {}".format(numOne, numTwo, func.sum(numOne, numTwo)))
print("Suma {} - {} : {}".format(numOne, numTwo, func.res(numOne, numTwo)))
print("Suma {} / {} : {:.2f}".format(numOne, numTwo, func.div(numOne, numTwo)))
print("Suma {} * {} : {}".format(numOne, numTwo, func.mul(numOne, numTwo)))