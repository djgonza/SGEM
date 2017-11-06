class Persona:

    def __init__(self, edad, sexo, pulsaRepo):
        self.__edad = edad
        self.__sexo = sexo
        self.__pulsaRepo = pulsaRepo

    def _getedad(self):
        return getattr(self, "_Persona__edad")

    def _setedad(self, edad):
        setattr(self, "_Persona__edad", edad)

    def _getsexo(self):
        return getattr(self, "_Persona__sexo")

    def _setsexo(self, sexo):
        setattr(self, "_Persona__sexo", sexo)

    def _getpulsa(self):
        return getattr(self, "_Persona__pulsaRepo")

    def _setpulsa(self, pulsaRepo):
        setattr(self, "_Persona__pulsaRepo", pulsaRepo)

    edad = property(fget=_getedad, fset=_setedad)
    sexo = property(fget=_getsexo, fset=_setsexo)
    pulsaRepo = property(fget=_getpulsa, fset=_setpulsa)

    """Los datos para calcular las pulsaciones máximas para hombres y mujeres se han sacado
    de la siguiente web: https://www.vitonica.com/entrenamiento/calcula-tu-frecuencia-cardiaca-maxima
    P.D: Se ha modificado haciendo un mix entre los corredores entrenados y los sedentarios."""
    def pulsacionmax(self):
        if self.sexo == "h":
            return 220 - (0.7 * self.edad)
        else:
            return 225 - (0.8 * self.edad)
