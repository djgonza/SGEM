from Act06.Ejercicio1.Prestamo import Prestamo

prestamoUno = Prestamo (12000, 5, 30)

print("PRESTAMO 1");
prestamoUno.toString();

pDosCapital = input ("Ingrese un Capital: ");
pDosInteres = input ("Ingrese un tipo de interes: ");
pDosAnno = input ("Ingrese años: ");

prestamoDos = Prestamo (pDosCapital, pDosInteres, pDosAnno);

print("PRESTAMO 2");
prestamoDos.toString();


