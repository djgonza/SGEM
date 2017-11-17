class Alarma:

    def __init__(self, hora=7, minuto=0):
        self.__hora = hora
        self.__minuto = minuto

    def _gethora(self):
        return getattr(self, "_Alarma__hora")

    def _getminuto(self):
        return getattr(self, "_Alarma__minuto")

    def _sethora(self, hora):
        setattr(self, "_Alarma__hora", hora)

    def _setminuto(self, minuto):
        setattr(self, "_Alarma__minuto", minuto)

    hora = property(fget=_gethora, fset=_sethora)
    minuto = property(fget=_getminuto, fset=_setminuto)

    def get_alarma(self):
        txthora = str(self.hora).zfill(2)
        txtminuto = str(self.minuto).zfill(2)
        return "{}:{}".format(txthora, txtminuto)

    def set_alarma(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto