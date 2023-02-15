#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import datetime
import codigoHTML
import os
from http import cookies

todasCokis={}   #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor)=elemCoki.split('=')
        todasCokis[nombre]=valor

    #todasCokis["SID"]="asdq4123d1"

if 'SID' in todasCokis:
    coki = cookies.SimpleCookie()
    #esta parte solo se ejecuta la primera vez que accede el usuario
    coki["SID"]=todasCokis["SID"]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) #enviar cookie caducada
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

print("Content-type: text/html\n")

print(codigoHTML.cabeceraHTML.format("CNI","Saliste del sistema"))
print("<a href='index.html'>página de acceso</a><br>")
print(codigoHTML.finHTML)