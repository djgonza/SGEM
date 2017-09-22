class Triangulo (object):

    def __init__(self, base,altura):
       self.base = base;
       self.altura = altura;

    def areaTriangulo(self):
        return self.base * self.altura / 2;