from Act11.Ejercicio02.Agenda import Agenda

agendita = {'Adela': '444444444', 'Pedro': '222222222', 'Bertoluchi': '777777777', 'Paco': '555555555', 'Berta': '666666666', 'Alba': '333333333', 'Ana': '111111111'}

agenda = Agenda(agendita)

nombre = input("Nombre a buscar: ").title()

if agenda.buscaragenda(nombre) == False:
    try:
        telefono = input("Introduzca un número de teléfono: ")
        agenda.telefonocorrecto(telefono)
        agenda.anadirtelefono(nombre, telefono)
        print("Contacto añadido")
    except AssertionError as err:
        print(err)
else:
    try:
        phone = agenda.buscaragenda(nombre)
        telefono = input("{}. Modificar {} (Enter:no modificar:) ".format(nombre, phone))
        agenda.telefonocorrecto(telefono)
        agenda.anadirtelefono(nombre, telefono)
        print("Agenda actualizada")
    except AssertionError as err:
        print(err)

agenda.tostring(agenda)