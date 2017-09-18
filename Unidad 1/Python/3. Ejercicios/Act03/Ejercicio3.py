frase =  input ("Teclea un carácter o una frase: ")

if frase.isspace():
    print("{} es un espacio en blanco".format(frase))
    exit()

if frase.istitle():
    print("{} es un title, la primera es mayúscula".format(frase))
    exit()

if frase.isalnum():
    print ("{} es alfanumérica, números y letras".format(frase))
else:
    print("{} NO es alfanumérica, números y letras".format(frase))

if frase.isalpha():
    print ("{} es letra o alfabética".format(frase))
elif frase.isdigit():
    print ("{} es numérico".format(frase))

if frase.islower():
    print("{} está en minuscula".format(frase))
else:
    print("{} está en mayuscula".format(frase))



