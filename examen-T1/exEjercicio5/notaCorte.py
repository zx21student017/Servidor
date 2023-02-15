#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi

#abrimos los ficheros
fNombres = open("nombres.dat","rt")
fNotas = open("notas.dat","rt")

#guardamos los datos de nombres y notas en dos variables
nombres = fNombres.read()
notas = fNotas.read()

#cerramos los ficheros
fNombres.close()
fNotas.close()

#dividimos el array de nombres y notas con espacios
nombres = nombres.split(" ")
notas = notas.split(" ")

#recuperamos la nota de corte
form = cgi.FieldStorage()
corte = form['corte'].value

#abrimos un fichero de salida en el que escribiremos el resultado
fSalida = open("salida.dat","wt")

cont = 0
for nomb in nombres:
    if notas[cont]>=corte:
        fSalida.write(nomb+" "+notas[cont]+"\n")
    cont+=1

fSalida.close()

print("Content-Type: text/html\n")

print("filtro realizado...")