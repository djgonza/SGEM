class ListaMinusMayus ():
    def __init__(self,lista):
        self.lista = lista
    def añadirnom (self,contador):
        acu = 0
        self.contador = contador
        while True:
            acu = acu + 1
            nombre = input("Nombre a añadir: ")
            self.lista.append(nombre)
            if acu == self.contador:
                break
        return self.lista



def main():

    list = ['Beñat', 'Xabi', 'Xabi', 'Maria', 'Alexander', 'Carlos', 'Juan', 'Imanol', 'Pedro', 'Uxue', 'Javier', 'Iker', 'Carlos', 'Xabi', 'Alejandra', 'Carolina', 'Iñaki', 'Asier', 'Maria']
    listus = ListaMinusMayus(list)

    contador = input("nombre a buscar: ")
    nuev =
    print ()
main()