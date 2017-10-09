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
        options = {"+":calculadora.sumar,"-":calculadora.restar,"*":calculadora.multiplicar,"/":calculadora.dividir}
        print(options[signo]())

print("Total operaciones: {}".format(Calculadora.contCalculos))
