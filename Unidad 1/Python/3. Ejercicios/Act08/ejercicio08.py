from ListaMinusMayus import ListaMinusMayus

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

miLista = ListaMinusMayus(lista)

nombre_a_borrar = input("Inserte el nombre a borrar: ")

listaNombres = miLista.nombre_posiciones(nombre_a_borrar)

contNombresBorrados = 0;
for posicion in listaNombres:
    accion = input("Nombre encontrado en la posicion {}, b (borrar), p (pasar): ".format(posicion))
    if accion == "b":
        del miLista.nombres[posicion - contNombresBorrados]
        contNombresBorrados += 1;
    elif accion == "p":
        print ("Pasado")
    else:
        print("Accion incorrecta")

miLista.title()