class Prestamo(object):

    def __init__(self, capital, tipoInteres, anno):
        try:
            self.capital = float(capital);
            self.tipoInteres = float(tipoInteres);
            self.anno = int(anno);
        except Exception as e:
            print(e);
            exit(0);

    def calcularInteres (self):
        return self.capital * self.tipoInteres * self.anno / 100;

    def toString (self):
        print("Capital: {}".format(self.capital));
        print("Interes: {}".format(self.tipoInteres));
        print("Anno: {}".format(self.anno));
        print("Total interes: {}".format(self.calcularInteres()));