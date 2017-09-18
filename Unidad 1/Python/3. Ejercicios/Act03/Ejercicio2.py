frase =  input ("Teclea una frase: ")
print ("En mayúsculas ", frase.upper())
print ("En minúsculas ", frase.lower())
print ("La letra más alta ", max(frase))
print ("La letra más baja ", min(frase))
letra = input("Teclea una letra de a-z: ").lower()
control = bool(0);

for i in frase:
    if i.lower() == letra:
        print ("{} SI esta en la frase {}".format(letra, frase))
        control = bool(1)
        break

if not control:
    print("{} NO esta en la frase {}".format(letra, frase))