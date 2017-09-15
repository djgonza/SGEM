import math
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

if a != 0:
    try:
        x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if x1 == x2:
            print('Solucion de la ecuacion: {} '.format(x1))
        else:
            print('Soluciones de la ecuacion: {} y {} '.format(x1, x2))
    except ValueError:
        print('Sin solucion real')
else:
    if b != 0:
        x = -c / b
        print('Solucion de la ecuacion: {} '.format(x))

    else:
        if c != 0:
            print ('La ecuacion no tiene solucion. ')

        else:
            print ('La ecuacion tiene infinitas soluciones.')