#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

#importamos las librerías
import cgi
import os
import json
import sys
import hashlib
import datetime
from http import cookies

#guardamos en args el valor dado
args = cgi.parse()

datos = []
existe = False

if "nombre" in args and "pass" in args and os.path.exists("datos/usuarios.json"):
    datos.append(args["nombre"][0])
    datos.append(args["pass"][0])

    f = open("datos/usuarios.json", "rt")
    datosJson = json.loads(f.read())
    f.close()

    for y in datosJson:
        for z in y:
            sys.strderr.write(">"+z+"<")
    
    for x in datosJson:
        datosNombre = x[0]
        datosEmail = x[1]
        datosPasswd = x[2]

        h=hashlib.sha512(str.encode(datos[1]))

        if datosNombre == datos[0] and datosPasswd == h.hexdigest():
            existe = True
            break
if existe:
    coki = cookies.SimpleCookie()
    coki["SID"] = "alskdjfhg"
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    coki['SID']['expires'] = expires.strftime("%a, %d, %b, %Y %H :%M :%S GMT")
    print(coki)

    print("Content-Type: text/plain\n")