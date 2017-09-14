print("Convertidor de segundos a minutos")
segundos = float(input("Escriba una cantidad de segundos: "))
segs = (segundos % 3600 / 60) % 60;
minutos = segundos % 3600 / 60;
horas = segundos // 3600;
print("{} segundos son {} horas {} minutos y {} segundos".format(segundos, horas, minutos, segs))