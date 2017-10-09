def pedirNumeros():
    while True:
        try:
            num = int(input("Teclea un número: "))
            print(num)
            break
        except ValueError:
            print("Debe ser número entero")

pedirNumeros()