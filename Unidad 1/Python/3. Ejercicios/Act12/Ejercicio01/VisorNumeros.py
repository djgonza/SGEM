class VisorNumeros:

    def __init__(self, limitemaximo):
        self.__limite = limitemaximo
        self.__valor = 0

    def _getvalor(self):
        return getattr(self, "_VisorNumeros__valor")

    def _getlimite(self):
        return getattr(self, "_VisorNumeros__limite")

    def _setvalor(self, valor):
        setattr(self, "_VisorNumeros__valor", valor)

    def _setlimite(self, limite):
        setattr(self, "_VisorNumeros__limite", limite)

    limite = property(fget=_getlimite, fset=_setlimite)
    valor = property(fget=_getvalor, fset=_setvalor)

    def __str__(self):
        txt = str(self.valor).zfill(2)
        return "{}".format(txt)

    def incrementar(self):
        if (self.valor >= self.limite - 1):
            self.valor = 0
        else:
            self.valor += 1