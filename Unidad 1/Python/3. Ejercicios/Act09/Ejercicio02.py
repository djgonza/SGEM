def pedirNumeros(num):
    try:
        return int(num)
    except ValueError:
        raise ValueError("Debe ser número entero")

while True:
    num = input("Teclea un número: ")
    try:
        print(pedirNumeros(num))
        break
    except ValueError as err:
        print(err)
