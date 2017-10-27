class Agenda(object):

    def __init__(self, agenda):
        self.__agenda = agenda

    def _getagenda(self):
        return getattr(self, "_Agenda__agenda")

    agenda = property(fget=_getagenda)

    def buscaragenda(self, nombre_buscar):
        if nombre_buscar in self.agenda:
            return self.agenda[nombre_buscar]
        else:
            return False

    @staticmethod
    def telefonocorrecto(telefono):
        assert (len(telefono) == 9), "Longitud del teléfono tiene que ser nueve y no {}".format(len(telefono))
        assert (telefono.isdigit()), "Introduzca solo números"
        return True

    def anadirtelefono(self, nombre, telefono):
        self.agenda.setdefault(nombre, telefono)

    @staticmethod
    def tostring(self):
        print(self)