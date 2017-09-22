class CocheITV (object):

    def __init__(self, matricula, anno):

        if self.validarMatricula(matricula):
            self.matricula = matricula;
        else:
            exit(0);
        self.anno = anno;

    def validarMatricula (self, matricula):

        try:
            splitMatricula = matricula.split("-");
            if not splitMatricula[0].isnumeric():
                raise Exception("Primeros digitos no numericos");
            if not len(splitMatricula[0]) == 4:
                raise Exception("Primeros digios longitud erronea");
            if not splitMatricula[1].isalnum():
                raise Exception("Ultimas letras no son letras");
            if not len(splitMatricula[1]) == 3:
                raise Exception("Ultimas letras longitud erronea");
            return bool(1)
        except Exception as e:
            print(e);
            return bool(0);

    def siguienteITV (self):
        return self.anno + 4;

    def toString(self):
        print("El coche con matricula {} del año {}, pasara la siguiente itv en el año {}".format(self.matricula, self.anno, self.siguienteITV()))
