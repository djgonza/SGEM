#Te pide que escribas un numero del 1 al 3 y si introduces otra cosa se repite (si no es un numero da error)
#Si introduces un numero de l-3  pasa a los if siguientes, si es 1 te devuelve "opcion 1" si es 2 nada y si es 3 se acaba
#En otro caso se repite puesto que no hay un break salvo en la opcion 3
while True:
   while True:
       op=int(input("Teclea opción (1-3. Para terminar 3 "))
       if op==1 or op==2 or op==3:
           break
   if op==1:
       print ("Opción 1")
   elif op==2:
       pass
   else:
       break
print ("ya se ha tecleado el 3")
while True:
   pass

