class Numero (object):

    def __init__(self, num):
        self.num = num

    def esPrimo(self):
        cont = 0
        i = 2
        if self.num == 1:
            return bool(0)
        else:
            while True:
                if i> self.num/2:
                    break

                if self.num % i == 0:
                    cont += 1
                if cont != 0:
                    return bool(0)
                i += 1
        return bool(1)