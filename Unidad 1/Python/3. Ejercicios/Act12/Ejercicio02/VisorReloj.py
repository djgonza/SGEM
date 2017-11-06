class VisorReloj:
    from Act12.Ejercicio01.VisorNumeros import VisorNumeros
    _visor_string = ""

    def __init__(self, hora=None, minuto=None):
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

    def _getvisor_string(self):
        return getattr(VisorReloj, "_visor_string")

    def _setvisor_string(self, string):
        setattr(VisorReloj, "_visor_string", string)

    visor_string = property(fget=_getvisor_string, fset=_setvisor_string)

    def actualizar_reloj(self):
        visor_string = "{}:{}".format(self.hora, self.minuto)

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