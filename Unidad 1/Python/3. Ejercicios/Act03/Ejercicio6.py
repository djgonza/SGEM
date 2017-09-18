password = input("Introduce contraseña: ")
longUser = len(password)

if longUser < 8:
    print ("La contraseña debe contener un mínimo de 8 caracteres")

correct = bool(1)
conNoAlfa = 0

for i in password:

    if i.isspace():
        correct = bool(0)
        break
    if i.isalpha():
        conNoAlfa += 1


if not correct or conNoAlfa <= 0:
    print ("Contraseña incorrecta")
else:
    print ("Contraseña correcta")