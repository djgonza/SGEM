from Act12.Ejercicio01.VisorNumeros import VisorNumeros

class VisorReloj:

    def __init__(self, hora=None, minuto=None):
        if hora == None and minuto == None:
            self.__hora = VisorNumeros(24)
            self.__minuto = VisorNumeros(60)
        else:
            self.__hora = hora
            self.__minuto = minuto

    def _gethora(self):
        return getattr(self, "_VisorReloj__hora")

    def _getminuto(self):
        return getattr(self, "_VisorReloj__minuto")

    def _sethora(self, hora):
        setattr(self, "_VisorReloj__hora", hora)

    def _setminuto(self, minuto):
        setattr(self, "_VisorReloj__hora", minuto)

    hora = property(fget=_gethora, fset=_sethora)
    minuto = property(fget=_getminuto, fset=_setminuto)

    def actualizar_reloj(self):
        return self

    def poner_en_hora(self, hora, minuto):
        self.hora.valor = hora
        self.minuto.valor = minuto
        self.actualizar_reloj()

    def emitir_tic(self):
        if self.minuto.valor == 59:
            self.hora.incrementar()
        self.minuto.incrementar()
        self.actualizar_reloj()

    def __str__(self):
        txtHora = self.hora
        txtMinuto = self.minuto
        return "{}:{}".format(txtHora, txtMinuto)