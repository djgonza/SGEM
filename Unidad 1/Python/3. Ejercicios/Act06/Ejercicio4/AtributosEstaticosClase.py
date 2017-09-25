class Prueba:

    attr = 0;

    def __init__(self, numero):
        self.numero = numero
    def incrementAttr (self, numero):
        Prueba.attr += numero


def main():
    cl1 = Prueba(3)
    cl2 = Prueba (4)
    cl3 = Prueba (9)
    cl1.incrementAttr(5);
    print(cl1.attr, cl1.numero)
    print(cl2.attr, cl2.numero)
    print(cl3.attr, cl3.numero)
    cl2.incrementAttr(10);
    print(cl1.attr, cl1.numero)
    print(cl2.attr, cl2.numero)
    print(cl3.attr, cl3.numero)
    cl3.incrementAttr(7);
    print(cl1.attr, cl1.numero)
    print(cl2.attr, cl2.numero)
    print(cl3.attr, cl3.numero)
main()