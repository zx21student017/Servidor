#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

#importamos las librerías
import cgi
from dbm import dumb
import codigoHTML as HTML 
import hashlib
import json
import os
import hashlib

print("Content-Type: text/plain\n")

#guardamos en args el valor dado
args = cgi.parse()

ruta = "datos/usuarios.json"

datos = []

if "nombre" in args and "correo" in args and "pass" in args:
    datos.append(args["nombre"][0])
    datos.append(args["correo"][0])

    h = hashlib.sha512(str.encode(args["pass"][0]))
    datos.append(h.hexdigest())

listaUsuarios=[]

if (os.path.exists(ruta)):
    f = open(ruta,"r")
    datosEnJson = json.loads(f.read())
    f.close()
    for valores in datosEnJson:

        datosDentro = []
        datosDentro.append(valores[0])
        datosDentro.append(valores[1])
        datosDentro.append(valores[2])

        listaUsuarios.append(datosDentro)

listaUsuarios.append(datos)

f = open(ruta,"w")

f.write(json.dumps(listaUsuarios))

f.close()

HTML.redReg()