from datetime import datetime
from Proyecto_Final.Clases.Persona import Persona
from Proyecto_Final.Clases.Sesion import Sesion

class RelojDeportivo:

    def __init__(self, persona, registros):
        self.persona = persona
        self.registros = registros

    def getPersona(self):
        return self.persona

    def getRegistros(self):
        return self.registros

    def horaActual(self):
        return datetime.now().time().strftime('%H:%M:%S')

    def distanciaTotal(self):
        total = 0
        for i in range(len(self.registros)):
            total += self.registros[i].distancia
        return total


