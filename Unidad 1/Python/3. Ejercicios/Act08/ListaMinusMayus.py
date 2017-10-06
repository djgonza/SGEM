class ListaMinusMayus:

    nombres = []

    def __init__(self, nombres):
        self.nombres = nombres

    def mayus(self):
        nombresUpper = []
        for nombre in self.nombres:
            nombresUpper.append(nombre.upper())
        print("Lista: ", nombresUpper)

    def minus(self):
        nombresLower = []
        for nombre in self.nombres:
            nombresLower.append(nombre.lower())
        print("Lista: ", nombresLower)

    def title(self):
        nombresTitle = []
        for nombre in self.nombres:
            nombresTitle.append(nombre.title())
        print("Lista: ", nombresTitle)

    def contar(self, busqueda):
        conta = 0
        for nombre in self.nombres:
             if nombre.lower() == busqueda.lower():
                 conta += 1
        print("Lista: ", conta)

    def nombre_posiciones(self,busqueda):
        posiciones = []
        for i in range(len(self.nombres)):
            if self.nombres[i].lower() == busqueda.lower():
                posiciones.append(i)
        if len(posiciones) == 0:
            return bool(0);
        else:
            return posiciones;

    def modificar_nombre(self, busqueda):
        for i in range(len(self.nombres)):
            if self.nombres[i].lower() == busqueda.lower():
                self.nombres[i] = input("Renombrar {} por: ".format(busqueda))
                return

