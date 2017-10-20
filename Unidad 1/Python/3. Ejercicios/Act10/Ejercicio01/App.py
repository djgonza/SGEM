from Act10.Ejercicio01.Agenda import Agenda

lista=[("Atanagildo Perez",694321567),
       ("Pedro Piqueras",948123456),
       ("Alba Gutierrez",9481356544),
       ("Adela",9481356588),
       ("Paco Palancia",9481356544),
       ("Berta Piqueras",9611356544),
       ("Pedro Piqueras",948222222),
       ("Bertoluchi Contreras",91381356544),
       ("Ana",9476656544),
       ("Paco Alloz",9481356544),
       ("Ana",947222222)]

agenda = Agenda(lista)

nombre = input("Nombre a buscar: ").title()

result = agenda.buscar_en_agenda(nombre)
if result == False:
   print("Contactos no encontrados")
else:
    print(nombre)
    agenda.telefonos(result)

