from Act12.Ejercicio02Nuevo.VisorReloj import VisorReloj

visor = VisorReloj()
print("Hora 1: {}".format(visor))
visor.emitir_tic()
print("Hora 1 + 1 minuto: {}".format(visor))

visor.poner_en_hora(23, 0)
print("Hora 2: {}".format(visor))
visor.emitir_tic()
print("Hora 2 + 1 minuto: {}".format(visor))

visor.poner_en_hora(12, 59)
print("Hora 3: {}".format(visor))
visor.emitir_tic()
print("Hora 3 + 1 minuto: {}".format(visor))

visor.poner_en_hora(23, 59)
print("Hora 4: {}".format(visor))
visor.emitir_tic()
print("Hora 4 + 1 minuto: {}".format(visor))
