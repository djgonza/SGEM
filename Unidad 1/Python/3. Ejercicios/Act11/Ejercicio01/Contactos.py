class Contactos(object):

    def __init__(self, lista):
        self.__agenda = lista

    def _getagenda(self):
        return getattr(self, "_Contactos__agenda")

    agenda = property(fget=_getagenda)

    def contactos_unificados(self):
        diccionario = {}
        for i in range(len(self.agenda)):
            correos = []
            nombre = self.agenda[i][0]
            contacto = self.agenda[i]

            for j in range(1, len(contacto)):
                correos.append(contacto[j])

            if nombre in diccionario:
                mails = []
                mails = diccionario.get(nombre)
                total = mails + correos
                diccionario.pop(nombre)
                diccionario.setdefault(nombre, total)
            else:
                diccionario.setdefault(nombre, correos)
        return diccionario