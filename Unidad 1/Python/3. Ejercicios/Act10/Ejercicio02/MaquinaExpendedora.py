class MaquinaExpendedora(object):

    _total = 0

    def __init__(self,precio):
        self.__precio = precio
        self.__importe = 0

    def _getimporte(self):
        return getattr(self,"_MaquinaExpendedora__importe")

    def _getprecio(self):
        return getattr(self, "_MaquinaExpendedora__precio")

    def _setimporte(self, importe):
        setattr(self,"_MaquinaExpendedora__importe",importe)

    def _setprecio(self,precio):
        setattr(self, "_MaquinaExpendedora__precio", precio)

    precio = property(fget=_getprecio, fset=_setprecio)
    importe = property(fget=_getimporte, fset=_setimporte)

    @staticmethod
    def gettotal():
        return getattr(MaquinaExpendedora, "_total")

    @staticmethod
    def settotal(valor):
        setattr(MaquinaExpendedora, "_total", valor)

    def insertar_dinero(self,cantidad):
        assert (cantidad > 0), "Introduzca una cantidad positiva"
        self.importe += cantidad
        dif = self.precio-self.importe
        assert self.precio <= self.importe, ("Introduzca más dinero, le faltan  {}  euros".format(dif))

    def imprimir_ticket(self):
        if self.importe >= self.precio:
            print("Imprimiendo ticket..... Ha introducido {} €".format(self.importe))
            total = MaquinaExpendedora.getTotal()
            total += self.precio
            MaquinaExpendedora.setTotal(total)
            self.devolver_cambios()
            return True
        else:
            self.cantidad_pendiente()
            return False


    def devolver_cambios(self):
        print("Que aproveche :)). No se olvide de su cambio : {}".format(self.importe-self.precio))
        print()

    def cantidad_pendiente(self):
        print("Introduzca más dinero, le faltan  {}  euros".format(self.precio-self.importe))

    def vaciar_maquina(self):
        print("")
        print("***********************************************************")
        print("Total recaudado por la máquina {}".format(MaquinaExpendedora.getTotal()))
        print("Vaciando máquina...")
        MaquinaExpendedora.setTotal(0)
        print("Máquina vaciada {}".format(MaquinaExpendedora.getTotal()))

