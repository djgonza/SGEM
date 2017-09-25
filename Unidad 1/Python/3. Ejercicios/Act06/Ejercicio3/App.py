from Act06.Ejercicio3.Cuadrado import Cuadrado
from Act06.Ejercicio3.Triangulo import Triangulo

print ("Cálculo de áreas")
print ("1 - Area de cuadrado")
print ("2 - Area de triangulo")
option = int(input ("Teclea una opcion (1 o 2): "))

if option == 1:
    cuadra = Cuadrado(float(input("Lado del cuadrado: ")))
    result = cuadra.areaCuadrado()
    print("Área del cuadrado: {}".format(result))
else:
    tria = Triangulo(float(input("Base: ")),float(input("Altura: ")))
    result = tria.areaTriangulo()
    print("Área del triangulo: {}".format(result))