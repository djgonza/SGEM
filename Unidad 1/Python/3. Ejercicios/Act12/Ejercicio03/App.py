from Act12.Ejercicio03.Alarma import Alarma
from Act12.Ejercicio03.RelojAlarma import RelojAlarma
from Act12.Ejercicio02Nuevo.VisorReloj import VisorReloj

visor_reloj = VisorReloj()
visor_reloj.poner_en_hora(6, 55)

alarm = Alarma()

reloj_alarm = RelojAlarma(visor_reloj, alarm)

for i in range(10):
    reloj_alarm.emitir_tic()

print()
print("*****************************************************************")
print()

""" En este caso nunca sonará la alarma ya que visor_reloj1 y la alarm1 no coinciden """
#Por defecto visor_reloj1 sera las 00:00
visor_reloj1 = VisorReloj()

#Por defecto alarm1 será las 07:00
alarm1 = Alarma()

reloj_alarm1 = RelojAlarma(visor_reloj1, alarm1)

for i in range(10):
    reloj_alarm1.emitir_tic()
