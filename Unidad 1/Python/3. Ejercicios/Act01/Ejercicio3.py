print("Convertidor de pies y pulgadas a centímetros")
pies = float(input("Escriba una cantidad de pies: "))
pulgadas = float(input("Escriba una cantidad de pulgadas: "))
cm = (pies * 12 + pulgadas) * 2.54;
print("{} pies y {} pulgadas son {} cm".format(pies, pulgadas, cm))
