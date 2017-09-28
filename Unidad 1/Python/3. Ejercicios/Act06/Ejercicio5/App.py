from Act06.Ejercicio5.Alumno import Alumno

alumno1 = Alumno("Maria", 8)
alumno2 = Alumno("Carlos", 6)

print(alumno1.nombre)  # María
print(alumno1.nota)  # 8

#alumno1.nombre = "Carmela"

print(Alumno.numalumnos)  # 2
print(Alumno.sumanotas)  # 14

print(alumno1.mostrarNombreNota())  # ('Carmen', 8)
print(alumno2.mostrarNombreNota())  # ('Carlos', 6)

del alumno1.nombre

#print(alumno1.mostrarNombreNota())

alumno1.nombre = "Carmen"