class Grados (object):

    def __init__(self, celsius, farenheit):
        self.celsius = celsius
        self.farenheit = farenheit

    def calcularCelsius(self):
        return ((self.farenheit - 32) * 5) / 9

    def calcularFarenheit(self):
        return (self.celsius * 9 / 5) + 32