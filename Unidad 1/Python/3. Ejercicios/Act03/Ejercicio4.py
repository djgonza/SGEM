email = input ("Dirección de e-correo: ")

emailParsed = email.split("@")

if emailParsed[1] == "gmail.com":
    print ("El email termina en gmail.com")
else:
    print ("El email no termina en gmail.com")

cont = 0
for i in email:
    if i == "@":
        cont += 1

print ("El email contiene {} @".format(cont))

print("@ esta en la posicion {}".format(email.find("@")))
print ("Usuario: {}".format(emailParsed[0]))
print ("Dominio: {}".format(emailParsed[1]))
