from Act09.Ejercicio04.Factorial import Factorial

while True:
    try:
        num = int(input("Número Entero >0: "))
        assert (num>=0),"El número debe ser mayor o igual a 0"
        factorial = Factorial(num)
        print("Factorial: {}".format(factorial.factorial()))
        break
    except ValueError:
        print("Debe ser número entero")
    except AssertionError as err:
        print(err)