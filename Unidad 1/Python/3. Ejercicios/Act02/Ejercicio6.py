a=int(input("Escriba un año y le diré si es bisiesto: "))
if(a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
    print("El año {} es un año bisiesto porque es múltiplo de 400".format(a))
elif a % 100 == 0 or a % 400 != 0:
    print("El año {} NO es un año bisiesto porque es múltiplo de 100 pero no es múltiplo de 400".format(a))
else:
    print("El año {} NO es un año bisiesto porque es múltiplo ni de 100 ni de 400".format(a))