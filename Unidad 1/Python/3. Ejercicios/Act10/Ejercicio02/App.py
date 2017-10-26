from Act10.Ejercicio02.MaquinaExpendedora import MaquinaExpendedora

maquinita = MaquinaExpendedora(0)

while True:
    try:
        cafes = int(input("¿Cuántos cafés quiere? "))
        print()
        assert (cafes > 0), "El número de cafés debe ser mayor de 0"
        break
    except ValueError:
        print("Debe introducir un valor numérico")
    except AssertionError as err:
        print(err)

for i in range(1, cafes+1):
    while True:
        try:
            precio = float(input("Cafe {}. Teclee su precio: ".format(i)))
            assert (precio > 0), "Introduzca una cantidad positiva"
            print("Supongo que quiere 1 CAFE y cuesta {}€".format(float(precio)))
            maquinita.precio = precio
            break
        except ValueError:
            print("Debe introducir un valor numérico")
        except AssertionError as err:
            print(err)

    while True:
        try:
            cantidad = float(input("¿Cuánto dinero mete en la máquina? "))
            maquinita.insertar_dinero(cantidad)
            break
        except ValueError:
            print("Debe introducir un valor numérico")
        except AssertionError as err:
            print(err)

    maquinita.imprimir_ticket()

maquinita.vaciar_maquina()
