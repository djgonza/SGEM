from ListaMinusMayus import ListaMinusMayus

lista = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos', 'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos', 'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

miLista = ListaMinusMayus(lista)

miLista.modificar_nombre(input("Introduce un nombre a buscar: "))
miLista.title()