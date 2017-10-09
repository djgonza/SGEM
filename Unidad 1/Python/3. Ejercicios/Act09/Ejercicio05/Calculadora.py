class Calculadora:

    contCalculos = 0

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        Calculadora.contCalculos += 1
        return self.num1 + self.num2

    def restar(self):
        Calculadora.contCalculos += 1
        return self.num1 - self.num2

    def multiplicar(self):
        Calculadora.contCalculos += 1
        return self.num1 * self.num2

    def dividir(self):
        Calculadora.contCalculos += 1
        return self.num1 / self.num2

    @staticmethod
    def leer_numero(prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                pass

    @staticmethod
    def leer_signo(prompt):
        while True:
            try:
                ope = input(prompt)
                assert (ope in ("+","-","*","/")),"Operando incorrecto"
                return ope
            except AssertionError:
                pass