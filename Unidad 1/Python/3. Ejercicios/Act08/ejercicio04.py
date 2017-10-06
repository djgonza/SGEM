from ListaMinusMayus import ListaMinusMayus

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

miLista = ListaMinusMayus(lista)

nombre = input("Nombre a buscar: ")
print("Está en las posiciones", miLista.nombre_posiciones(nombre))