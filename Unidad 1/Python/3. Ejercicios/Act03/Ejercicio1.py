print ("Recorrer cadena")
frase =  input ("Teclea una frase: ")
longi = len(frase)
for i in frase:
    print (i)
pos = int(input ("Teclea una posición: "))
if pos < 1 or pos > longi:
    print("ERROR")
else:
    print("Desde el Inicio: posicion {} Carácter {}".format(pos,frase[pos-1]))
    print("Desde el Final: posicion {} Carácter {}".format(pos, frase[-pos]))
    print("los primeros {} caracteres: {} ".format(pos, frase[0:pos]))
    print("los últimos {} caracteres: {} ".format(pos, frase[-pos:]))