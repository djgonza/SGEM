from Act12.Ejercicio01.VisorNumeros import VisorNumeros
from Act12.Ejercicio02Nuevo.VisorReloj import VisorReloj

class RelojAlarma:

    def __init__(self, visor_reloj, alarma):
        self.visor_reloj = visor_reloj
        self.alarma = alarma

    def set_alarma(self, hora, minuto):
        self.alarma.set_alarma(hora, minuto)

    def get_hora(self):
        return self.visor_reloj

    def get_alarma(self):
        return self.alarma.get_alarma()

    def _es_hora(self):
        return str(self.get_hora()) == str(self.get_alarma())

    def emitir_tic(self):
        self.visor_reloj.emitir_tic()
        print(self.visor_reloj)
        if self._es_hora():
            print("RIIIIIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNNNNNNGGGGGGGGGGGGGGGGGGGGGGGGGGGG!!!!!")

