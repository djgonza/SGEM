print("Comparador de TRES numeros")
numOne = int(input("Escriba un numero: "))
numTwo = int(input("Escriba otro: "))
numThree = int(input("Escriba otro: "))

if numOne == numTwo & numTwo == numThree:
    print("Has escrito tres veces el número")
elif numOne == numTwo or numTwo == numThree or numOne == numThree:
    print("Has escrito uno de los números dos veces")
else:
    print("Los tres números son distintos")