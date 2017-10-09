def leerOpcion(opcion):
    opcion = opcion.upper()
    assert opcion in ("A","B","M"),"Opción no es A-B-M"
    return opcion

while True:
    try:
        opcion = input("Ingresa A (Altas) - B (Bajas) - M (Modificaciones): ")
        print(leerOpcion(opcion))
        break
    except AssertionError as err:
        print(err)