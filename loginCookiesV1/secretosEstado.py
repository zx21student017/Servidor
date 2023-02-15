#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os
from http import cookies

usuarios = {"pepe":["1234","asdqwe1"],"maria":["1111","asd123a"]}
estasDentro = False

todasCokis={}   #diccionario vacio
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE']
    listaCoki = listaCoki.split('; ')

    for elemCoki in listaCoki:
        (nombre, valor)=elemCoki.split('=')
        todasCokis[nombre]=valor

    #todasCokis["SID"]="asdq4123d1"

agente = ""

if 'SID' in todasCokis: #todasCokis
    for agen,datos in usuarios.items():
        if(datos[1] == todasCokis["SID"]):
            estasDentro = True
            agente=agen

print("Content-type: text/html\n")

if estasDentro:
    print(codigoHTML.cabeceraHTML.format("CNI","Secretos de estado"))
    print("<h6 class='Display-6'>Estas dentro, bienvenido agente "+agente+"</h6>")
    print("<a href='login.py'>Volver</a><br>")
    print("<a href='logout.py'>Salir</a><br>")
    print(codigoHTML.finHTML)
else:
    print(codigoHTML.codigoHTML.format("CNI","Error de acceso"))
    print("<h6 class='Display-6'>Llamando a la polisia</h6>")
    print("<a href='login.py'>Volver</a><br>")
    print(codigoHTML.finHTML)