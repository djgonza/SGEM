class CreaUsuario:

    def __init__(self, nombreCompleto):
        self.nombreCompleto = nombreCompleto

    def crearUsuario (self):

        print(self.nombreCompleto)

        username = ""
        username += self.nombreCompleto[0][0:2]
        username += self.nombreCompleto[1][0][0:2]
        username += self.nombreCompleto[1][1][0:3]
        return username