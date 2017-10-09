class Factorial:

    def __init__(self,numero):
        self.numero = numero

    def factorial(self):
        fact = 1
        for i in range(1,self.numero):
            fact += fact * i
        return fact
