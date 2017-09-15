import math

print ("a) Triangulo")
print ("b) Circulo")

opt = input("¿Qué figura quiere calcular (Escriba T o C)?")

if opt == "c":
    radio = float(input("Inserte un radio: "))
    result = rad ** 2 * math.pi
    print ("Un círculo de radio {} tiene un área de {}".format(radio, result))
elif opt == "t":
    base = float(input("Inserte la base: "))
    altura = float(input("Inserte la altura: "))
    result = base * altura / 2
    print ("Un triángulo de base {} y altura {} tiene un área de {}".format(base, altura, result))
else:
    print("Opcion incorrecta")
