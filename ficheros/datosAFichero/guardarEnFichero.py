#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi
import json

print("Content-Type: text/plain\n")

args = cgi.parse()

datos = []

datos.append(args["nombre"][0])
datos.append(args["edad"][0])

print(json.dumps(datos))

f = open("datos/listado.json","a")
f.write(json.dumps(datos))
f.close()