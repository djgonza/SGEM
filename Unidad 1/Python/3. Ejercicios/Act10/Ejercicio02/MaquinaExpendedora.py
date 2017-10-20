class MaquinaExpendedora(object):

    _total = 0

    def __init__(self,precio):
        self.__precio = precio
        self.__importe = 0

    def _getImporte(self):
        return getattr(self,"_MaquinaExpendedora__importe")

    def _getPrecio(self):
        return getattr(self, "_MaquinaExpendedora__precio")

    def _setImporte(self, importe):
        setattr(self,"_MaquinaExpendedora__importe",importe)

    def _setPrecio(self,precio):
        setattr(self, "_MaquinaExpendedora__precio", precio)

    precio = property(fget=_getPrecio())
    importe = property(fget=_getImporte())

    def getTotal(self):
        getattr(MaquinaExpendedora, "_total")

    def setTotal(self, valor):
        setattr(MaquinaExpendedora, "_total",valor)

    def insertar_dinero(self,cantidad):
        if cantidad > 0:
            print("")
        else:
            print("Introduzca una cantidad positiva")

    def imprimir_ticket(self):
        print("Imprimiendo ticket..... Ha introducido {} €".format(self.importe))
        self.devolver_cambios()

    def devolver_cambios(self):
        print("Que aproveche :)). No se olvide de su cambio : {}".format(self.importe-self.precio))

    def cantidad_pendiente(self):
        print("Introduzca más dinero, le faltan  {}  euros".format(self.precio-self.importe))

    def vaciar_maquina(self):
        print("Total recaudado por la máquina {}".format(self.getTotal()))
        print("Vaciando máquina...")
        self.setTotal(0)
        print("Máquina vaciada {}".format(self.getTotal()))