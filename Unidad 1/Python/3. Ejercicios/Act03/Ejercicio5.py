user = input("Introduce nombre de usuario: ")
longUser = len(user)

if longUser < 6:
    print ("El nombre de usuario debe contener al menos 6 caracteres")
elif longUser > 12:
    print("El nombre de usuario no puede contener más de 12 caracteres")
elif not user.isalnum():
    print ("El nombre de usuario puede contener solo numeros y letras")
else:
    print ("Nombre de usuario correcto")