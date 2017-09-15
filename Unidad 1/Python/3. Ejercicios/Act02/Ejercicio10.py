cmi = int(input ("Inserte una distacia (cm): "))

if cmi >= 100000 :
	km = int(cmi / 100000)
	m = int((cmi - km * 100000) / 100)
	cm = cmi - (km * 100000 + m * 100)
	print ("{}cm son {}km {}m y {}cm".format(cmi, km, m, cm))
elif cmi >= 100 :
	m = int(cmi / 100)
	cm = cmi - m * 100
	print ("{}cm son {}m y {}cm".format(cmi, m, cm))
else :
	print ("{}cm son {}cm".format(cmi, cmi)) 