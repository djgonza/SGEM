class Grados (object):

    def __init__(self, celsius, farenheit):
        self.celsius = celsius
        self.farenheit = farenheit

    def calcularCelsius(self):
        return ((self.farenheit - 32) * 5) / 9

    def calcularFarenheit(self):
        return (self.celsius * 9 / 5) + 32

gradetes = 10;
contador = 1;

while True:
    if contador == 11:
        break
    grados = Grados(0,gradetes)
    print("{} F = {:.5} C".format(gradetes, grados.calcularCelsius()))
    gradetes += 10
    contador += 1