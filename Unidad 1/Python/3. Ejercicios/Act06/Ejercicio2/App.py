from Act06.Ejercicio2.CocheITV import CocheITV

inputMatricula = input("Inserte una matricula: ");
inputAnno = int(input("Inserte un año: "));
coche = CocheITV(inputMatricula, inputAnno);
coche.toString();