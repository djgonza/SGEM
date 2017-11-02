class MaquinaExpendedora(object):

    _total = 0

    def __init__(self):
        self.__importe = 0
        self.__precio = 0
        self.__productos = {'Cafe': (1.1, 5),
                            'Agua': (0.8, 2),
                            'Palomitas': (1.5, 4),
                            'Aquarius': (1.5, 3),
                            'Chaskis': (1.0, 10),
                            'KitKat': (2.5, 0)}

    def _getimporte(self):
        return getattr(self,"_MaquinaExpendedora__importe")

    def _getprecio(self):
        return getattr(self,"_MaquinaExpendedora__precio")

    def _setimporte(self, importe):
        setattr(self,"_MaquinaExpendedora__importe",importe)

    def _setprecio(self, precio):
        setattr(self,"_MaquinaExpendedora__precio",precio)

    def _getproductos(self):
        return getattr(self, "_MaquinaExpendedora__productos")

    productos = property(fget=_getproductos)
    importe = property(fget=_getimporte, fset=_setimporte)
    precio = property(fget=_getprecio, fset=_setprecio)

    @staticmethod
    def gettotal():
        return getattr(MaquinaExpendedora, "_total")

    @staticmethod
    def settotal(valor):
        setattr(MaquinaExpendedora, "_total", valor)

    def mostrarproductos(self):
        products = self.productos.keys()
        print("**** MÁQUINA EXPENDEDORA ****")
        for prod in products:
            datos = self.productos[prod]
            precio = datos[0]
            unidades = datos[1]
            print("{} \nPrecio:{} € = Unidades:{} unidades".format(prod, precio, unidades))
            print("----------")
        print("")

    def existeproducto(self, nombreprod):
        if nombreprod in self.productos:
            return True
        print("Producto no existe, vuelva a teclear.")
        return False

    def precioproducto(self, nombreprod):
        return self.productos[nombreprod][0]

    def unidadesproducto(self, nombreprod):
        return self.productos[nombreprod][1]

    def comprobarunidades(self, nombreprod, unidades):
        uni = self.unidadesproducto(nombreprod)
        if uni < unidades:
            print("Del producto {} solo hay {} unidades.".format(nombreprod, uni))
            return False
        self.restarunidades(nombreprod, unidades)
        return True

    def restarunidades(self, nombreprod, unidades):
        precio = self.precioproducto(nombreprod)
        uni = self.unidadesproducto(nombreprod) - unidades
        array = (precio, uni)
        self.productos.pop(nombreprod)
        self.productos.setdefault(nombreprod, array)

    def insertar_dinero(self, nombreProducto, unidades, importe):
        assert (importe > 0), "Introduzca un importe positivo"
        self.importe += importe
        self.precio = self.precioproducto(nombreProducto) * unidades
        dif = self.precio-self.importe
        assert self.precio <= self.importe, ("Introduzca más dinero, le faltan  {}  euros".format(dif))

    def imprimir_ticket(self):
        if self.importe >= self.precio:
            print("Imprimiendo ticket..... Ha introducido {} €".format(self.importe))
            total = MaquinaExpendedora.gettotal()
            total += self.precio
            MaquinaExpendedora.settotal(total)
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
        print("Total recaudado por la máquina {}".format(MaquinaExpendedora.gettotal()))
        print("Vaciando máquina...")
        MaquinaExpendedora.settotal(0)
        print("Máquina vaciada {}".format(MaquinaExpendedora.gettotal()))

