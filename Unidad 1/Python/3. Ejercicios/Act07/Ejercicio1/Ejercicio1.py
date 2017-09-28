#Lo que hace este ejercicio es pedirte que teclees 1,2 o 3.
#Si escribes 1, imprime Opción 1
#Si escribes 2, "pasa" y vuelve a pedirte que teclees un número.
#Si escribes 3, imprime el texto "Ya se ha tecleado 3"
#Si se teclea cualquier número pide que escribas una opción indefinidamente.
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
