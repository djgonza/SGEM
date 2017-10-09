from Act09.Ejercicio05.Calculadora import Calculadora

while True:
    num1 = Calculadora.leer_numero("Primer operando (0:Terminar): ")
    if num1 == 0:
        break
    signo = Calculadora.leer_signo("Signo (+, -, *, /): ")
    num2 = Calculadora.leer_numero("Segundo operando: ")
    if num2 == 0:
        print("Divisor es 0")
    else:
        calculadora = Calculadora(num1,num2)
        if signo == "+":
            print("Resultado suma: {}".format(calculadora.sumar()))
        elif signo == "-":
            print("Resultado resta: {}".format(calculadora.restar()))
        elif signo == "*":
            print("Resultado multiplicación: {}".format(calculadora.multiplicar()))
        else:
            print("Resultado división: {}".format(calculadora.dividir()))

print("Total operaciones: {}".format(Calculadora.contCalculos))
