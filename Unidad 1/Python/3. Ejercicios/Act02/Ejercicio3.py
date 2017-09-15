import datetime
thisYear = datetime.datetime.now().year
otherYear = int(input("Inserte un año: "))
if thisYear > otherYear:
    print("Desde el año {} han pasado {} años".format(otherYear, (thisYear - otherYear)))
elif thisYear < otherYear:
    print ("Para llegar al año {} faltan {} años".format(thisYear, (otherYear - thisYear)))
else:
    print ("Son el mismo AÑO!!!!!!")