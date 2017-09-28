from Act07.Ejercicio2.Prestamo import Prestamo

print("Datos del préstamo")

while True:
    capital = input("Capital (0=Salir): ")
    if not capital.isnumeric():
        pass
    elif capital == "0":
        break
    elif capital.isalpha():
        pass
    else:
        capital = float(capital)
        tipointeres = float(input("Tipo de interés %:"))
        años = float(input("Años: "))
        prestamo = Prestamo(capital, tipointeres, años)
        print("Total intereses: {}".format(prestamo.calcularInteres()))

print("")
Prestamo.mostrar(Prestamo)