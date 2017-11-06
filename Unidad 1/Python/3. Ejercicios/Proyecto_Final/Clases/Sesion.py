class Sesion:

    def __init__(self, horaInicio, horaFin, distancia, pulsaMin):
        self.__horaInicio = horaInicio
        self.__horaFin = horaFin
        self.__distancia = distancia
        self.__pulsaMin = pulsaMin

    def _gethoraInicio(self):
        return getattr(self, "_Sesion__horaInicio")

    def _sethoraInicio(self, horaInicio):
        setattr(self, "_Sesion__horaInicio", horaInicio)

    def _gethoraFin(self):
        return getattr(self, "_Sesion__horaFin")

    def _sethoraFin(self, horaFin):
        setattr(self, "_Sesion__horaFin", horaFin)

    def _getdistancia(self):
        return getattr(self, "_Sesion__distancia")

    def _setdistancia(self, distancia):
        setattr(self, "_Sesion__distancia", distancia)

    def _getpulsaMin(self):
        return getattr(self, "_Sesion__pulsaMin")

    def _setpulsaMin(self, pulsaMin):
        setattr(self, "_Sesion__pulsaMin", pulsaMin)

    horaInicio = property(fget=_gethoraInicio, fset=_sethoraInicio)
    horaFin = property(fget=_gethoraFin, fset=_sethoraFin)
    distancia = property(fget=_getdistancia, fset=_setdistancia)
    pulsaMin = property(fget=_getpulsaMin, fset=_setpulsaMin)
