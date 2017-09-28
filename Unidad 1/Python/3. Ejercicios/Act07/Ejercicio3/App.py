from Act07.Ejercicio3.Grados import Grados

gradetes = 10;
contador = 1;

while True:
    if contador == 11:
        break
    grados = Grados(0,gradetes)
    print("{} F = {:.5} C".format(gradetes, grados.calcularCelsius()))
    gradetes += 10
    contador += 1