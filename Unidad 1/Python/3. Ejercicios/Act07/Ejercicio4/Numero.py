class Numero (object):

    def __init__(self, num):
        self.num = num

    def esPrimo(self):
        cont = 0
        if self.num == 1:
            return bool(0)
        for i in range(self.num):
            if self.num % i == 0:
               cont += 1
            if cont != 0:
                return bool(0)
        return bool(1)