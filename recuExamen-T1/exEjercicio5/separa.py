#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi

#abrimos el fichero de los alumnos
fdatos = open("datos.dat","rt")
#guardamos los datos del fichero en una variable
alumnos = fdatos.read()
#cerramos los ficheros
fdatos.close()

#dividimos el array de nombres y notas con espacios
alumnos = alumnos.split(" ")

#abrimos los ficheros de salida de suspenso y aprobado
fAprobados = open("aprobados.dat","wt")
fSuspensos = open("suspensos.dat","wt")

for alum in alumnos:
    if alumnos[1]>=5:
        fAprobados.write(alumnos)
    else:
        fSuspensos.write(alumnos)

fAprobados.close()
fSuspensos.close()

print("Content-Type: text/html\n")

print("separación realizada...")