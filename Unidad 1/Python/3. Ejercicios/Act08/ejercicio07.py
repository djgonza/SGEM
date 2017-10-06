from ListaMinusMayus import ListaMinusMayus

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

miLista = ListaMinusMayus(lista)

cantidadAnadir = int(input("Cantidad alumnos a añadir: "))

for i in range(cantidadAnadir):
    nombreAnadir = input("Nombre a añadir: ")
    if miLista.nombre_posiciones(nombreAnadir):
        print("El nombre ya existe")
    else:
        miLista.nombres.append(nombreAnadir.title())

miLista.title();