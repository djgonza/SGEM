class Agenda(object):
    def __init__(self,lista):
        self.__agenda = lista

    def _getAgenda(self):
        return getattr(self, "_Agenda__agenda")
        # return self.__agenda

    agenda = property(fget=_getAgenda)

    def buscar_en_agenda(self, nombre):
        resultado = []
        for i in range(len(self.agenda)):
            listado = self.agenda[i]
            nombreLista = listado[0].title()
            if nombreLista == nombre:
                resultado.append(listado)
        if len(resultado) == 0:
            return bool(0)
        else:
            return resultado

    def telefonos(self,lista):
        for i in range(len(lista)):
            print(lista[i][1])
