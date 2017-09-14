print("Convertidor de grados Farhrenheit a grados Celsius")
farenheit = float(input("Escriba una temperatura en grados Farenheit: "))
celsius = (farenheit - 32) / 1.8;
print("{:.2f} ºC equivalen a {:.2f} ºF".format(celsius, farenheit))