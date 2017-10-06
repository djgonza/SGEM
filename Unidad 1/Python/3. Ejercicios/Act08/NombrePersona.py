class NombrePersona:

    nombre = ""
    apll = ""

    def __init__(self, nombre, apll):
        self.nombre = nombre.title()
        self.apll = apll.title()

    def mostrar(self):
        nombreParseado = self.nombre.split(" ")
        iniciales = ""

        for nombre in nombreParseado:
            iniciales += nombre[0].upper() + ". "

        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apll)
        print("Iniciales: ", iniciales)
        print(iniciales, ", ", self.apll)
        print(self.apll, ", ", self.nombre)
