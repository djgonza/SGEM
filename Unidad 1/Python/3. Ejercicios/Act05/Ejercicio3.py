import Act05.ej3.archivo as archivo

print ("1 - Area de cuadrado")
print ("2 - Area de triangulo")
option = int(input ("Teclea una opcion (1 o 2): "))

if option == 1 :
    result = archivo.areaCuadrado(float(input("Lado del cuadrado: ")))
    print("Área del cuadrado: {}".format(result))
else:
    base = float(input("Base del triangulo: "))
    altura = float(input("Altura del triangulo: "))
    result = archivo.areaTriangulo(base, altura)
    print ("Área del triangulo: {}".format(result))

num = input("Inserte un numero: ")
result = archivo.parseMensaje(num)
print("Entero {} Real {} y String {}".format(result[0],result[1],result[2]))