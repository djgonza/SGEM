from Act12.Ejercicio02.VisorReloj import VisorReloj
from Act12.Ejercicio01.VisorNumeros import VisorNumeros

"""Creamos un visor Reloj sin pasarle ningun parámetro Hora y Minuto de la clase VisorNumeros, 
por defecto establece la hora 00:00"""
visor = VisorReloj()
print("Una hora inicializada a las: {}".format(visor))
for i in range(60):
   visor.emitir_tic()
   if i == 30:
      print(visor)
   else:
      print(visor, end=" ")

"""Creamos dos objetos hora y minuto de la clase VisorNumeros, les establecemos para que la hora
sea las 15:45. Por último con el método de la clase VisorReloj, ponemos en hora."""
hora = VisorNumeros(24)
minuto = VisorNumeros(60)
hora.valor = 15
minuto.valor = 45
visor.poner_en_hora(hora.valor, minuto.valor)
print("\n\nUna hora inicializada a las: {}".format(visor))

for i in range(60):
   visor.emitir_tic()
   if i == 30:
      print(visor)
   else:
      print (visor, end=" ")