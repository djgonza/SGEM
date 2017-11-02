from Act11.Ejercicio03.MaquinaExpendedora import MaquinaExpendedora

maquinita = MaquinaExpendedora()

maquinita.mostrarproductos()

nombre = input("Introduzca el nombre del producto que quiera comprar").title()
while True:
    if maquinita.existeproducto(nombre):
        break
        nombre = input("Introduzca el nombre del producto que quiera comprar: ").title()

while True:
    try:
        unidades = int(input("¿Cuántas unidades quieres comprar?"))
        assert (unidades > 0), "Debe comprar al menos una unidad del producto seleccionado"
        if maquinita.comprobarunidades(nombre, unidades):
            break
    except ValueError:
        print("Debe introducir un valor numérico")
    except AssertionError as err:
        print(err)

precio = maquinita.precioproducto(nombre) * unidades
print("Ha seleccionado {} => {} unidad/es, su precio es {}€".format(nombre, unidades, precio))

while True:
    try:
        importe = float(input("¿Cuánto dinero mete en la máquina? "))
        maquinita.insertar_dinero(nombre, unidades, importe)
        break
    except ValueError:
        print("Debe introducir un valor numérico")
    except AssertionError as err:
        print(err)

maquinita.imprimir_ticket()

maquinita.mostrarproductos()

maquinita.vaciar_maquina()