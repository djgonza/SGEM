ele = int(input("Cuántos nombres tiene la lista: "))
acu = 0
lista = []
while True:
    acu = acu+1
    nombre = input("Nombre "+str(acu)+": ")
    lista.append(nombre)
    if acu == ele:
        break
print("La lista creada es:",lista)
