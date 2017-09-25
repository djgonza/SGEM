from Act06.Ejercicio4.Factura import Factura

print("-- FACTURA --");

baseImponible = float(input("Introduzca BASE IMPONIBLE: "));

discount = input("¿ Hay descuento? s/n");
if discount.lower() == "s":
    descu = 10;
elif discount.lower() == "n":
    descu = 0;
else:
    print("Debe escribir 's' para SI o 'n' para NO")
    exit()

iv = input("¿ Que tipo de IVA se aplicará: General(g) o Reducido(r)?")
if iv.lower() == "g":
    iva = 21;
elif iv.lower() == "r":
    iva = 6;
else:
    print("Debe introducir o 'G' para General o 'R' para Reducido")
    exit()

factura = Factura(baseImponible,descu,iva)
print("La factura con BASE IMPONIBLE {}".format(baseImponible))
print("Tiene un {} % de descuento y quedaria {}".format(descu, factura.base_con_descuento()))
print("Se aplica un {} % de IVA y su valor es {}".format(iva,factura.total_iva_incluido()))