class ListaMinusMayus ():
    def __init__(self,lista):
        self.lista = lista

    def a_mayus(self):
        for cont, elemento in enumerate (self.lista):
            mayus = elemento.upper()
            self.lista[cont]=mayus
        return self.lista
    def a_minus(self):
        for cont, elemento in enumerate(self.lista):
            minus = elemento.lower()
            self.lista[cont] = minus
        return self.lista
    def a_title(self):
        for cont, elemento in enumerate(self.lista):
            capit = elemento.capitalize()
            self.lista[cont] = capit
        return self.lista
    def cuenta_nombre(self,nombre):
        self.nombre = nombre
        for cont, elemento in enumerate(self.lista):
            minus = elemento.lower()
            self.lista[cont] = minus
        return self.lista.count(self.nombre)

def main():

    list = ['Beñat', 'XaBi', 'Xabi', 'MARIA', 'Alexander', 'Carlos',
            'JUAN', 'Imanol', 'PEDRO', 'Uxue', 'javier', 'iker', 'carlos',
            'Xabi', 'ALEJANDRA', 'cAROLINA', 'iÑaKI', 'Asier', 'Maria']

    listus = ListaMinusMayus(list)

    print ("Lista original ",list)
    mayu = listus.a_mayus()
    print ("Lista en MAYÚSCULAS ",mayu)
    minu = listus.a_minus()
    print ("Lista en minúsculas ",minu)
    capi = listus.a_title()
    print ("Lista en Title ",capi)
    print("")
    nombre = input("nombre a buscar: ")
    print (nombre," aparece ",listus.cuenta_nombre(nombre)," veces" )

main()
#for elemento in lista:
    #print(elemento)

# lista.extend("palabra")   -añade palabra separando las letras
# lista.count("nombre")  -contar veces que aparece
# del.lista[posicion]
# lista.remove("nombre")