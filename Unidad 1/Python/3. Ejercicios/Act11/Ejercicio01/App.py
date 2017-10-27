from Act11.Ejercicio01.Contactos import Contactos

lista = [('Ana', 'correo1@ana.es', 'correo2@ana.es'), ('Maria', 'correo1@maria.es'), ('Iker', 'correo1@iker.es'), ('Ana', 'correo3@ana.es', 'correo4@ana.es'), ('Iker', "correo'2@iker.es"), ('Ana', 'correo5@ana.es')]

contactitos = Contactos(lista)

diccionario = contactitos.contactos_unificados()

for contacto in diccionario:
    print("{} {}".format(contacto, diccionario.get(contacto)))