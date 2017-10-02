class Prestamo (object)
    cuenta_prestamos = 0
    acumula_prestamos = 0
    acumula_intereses = 0

    def __init__(self, capital, tipointeres, años):
        self.capital = capital
        self.tipointeres = tipointeres
        self.años = años
        Prestamo.cuenta_prestamos += 1
        Prestamo.acumula_prestamos += self.capital
        Prestamo.acumula_intereses += self.tipointeres

while True:
    print ("Datos préstamo")
    ele = input("Capital (0=salir:) ")
    if ele == "0":
        break
    if ele.isalpha():
        pass





