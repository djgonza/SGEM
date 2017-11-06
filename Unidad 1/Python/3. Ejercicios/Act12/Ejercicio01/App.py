from Act12.Ejercicio01.VisorNumeros import VisorNumeros

hora = VisorNumeros(24)
minuto = VisorNumeros(60)

print ("Hora: ")
for i in range(90):
   hora.incrementar()
   print (hora, end="-")

print("\n")

print("Minuto: ",)
for i in range(90):
   minuto.incrementar()
   print(minuto, end="-")