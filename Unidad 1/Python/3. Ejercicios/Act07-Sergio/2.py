class Prestamo (object):

    cuenta_prestamos = 0
    acumula_prestamos = 0
    acumula_intereses = 0

    def __init__(self, capital, tipointeres, anos):
        self.capital = capital
        self.tipointeres = tipointeres
        self.anos = anos
        Prestamo.cuenta_prestamos += 1
        Prestamo.acumula_prestamos += capital
        Prestamo.acumula_intereses += self.calcularInteres()

    def mostrar(self):
        print("Total de préstamos: {}".format(self.cuenta_prestamos))
        print("Capital prestado: {}".format(self.acumula_prestamos))
        print("Total de intereses: {}".format(self.acumula_intereses))

    def calcularInteres(self):
        return self.capital * self.tipointeres * self.anos / 100

    print ("Datos préstamo")
while True:
    ele = input("Capital (0=salir:) ")
    if ele == "0":
        break
    inte = input("Tipo de interés %: ")
    anio = input("Años: ")
    if  ele.isnumeric() and int(inte) > -1 and int(anio) > -1:
        pres1=Prestamo(float(ele),float(inte),float(anio))
        total_inte= pres1.calcularInteres()
        print("Total intereses ", (total_inte))


Prestamo.mostrar(Prestamo)
