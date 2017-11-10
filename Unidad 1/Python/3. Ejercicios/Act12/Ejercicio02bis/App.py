from Act12.Ejercicio02bis.VisorReloj import VisorReloj
from Act12.Ejercicio01.VisorNumeros import VisorNumeros

hora = VisorNumeros(24)
minuto = VisorNumeros(60)

horaInicial = input("Una hora inicializada(HH:MM) a las: ")

pos = horaInicial.find(":")
h = int(horaInicial[0:pos])
m = int(horaInicial[pos+1:])

while True:
    if not h > 23 or m > 50:
        break
    horaInicial = input("Una hora inicializada(HH:MM) a las: ")
    h = int(horaInicial[0:pos])
    m = int(horaInicial[pos + 1:])

hora.valor = h
minuto.valor = m

visor = VisorReloj(hora,minuto)

for i in range(60):
   visor.emitir_tic()
   print (visor, end=" ")