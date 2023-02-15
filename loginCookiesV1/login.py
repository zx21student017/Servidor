#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi
import datetime
import codigoHTML
import os
from http import cookies

usuarios = {"pepe":["1234","asdqwe1"],"maria":["1111","asd123a"]}

args = cgi.parse()
user = args['usuario'][0]
passwd = args['pass'][0]
estaDentro = False

if user in usuarios:
    if usuarios[user][0] == passwd:
        estaDentro = True

if estaDentro:
    coki = cookies.SimpleCookie()
    #esta parte solo se ejecuta la primera vez que accede el usuario
    coki["SID"]=usuarios[user][1]
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=30) #expira en 30 dias
    coki['SID']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

print("Content-type: text/html\n")

print(codigoHTML.cabeceraHTML.format("CNI","Entrada al CNI"))

if estaDentro:
    print("<h6 class='Display-6'>Estas dentro</h6>")
    print("<a href='secretosEstado.py'>Secretos de Estado</a><br>")
    print("<a href='login.py'>Secretos del Emerito</a><br>")
    print(codigoHTML.finHTML)

else:
    print(codigoHTML.redireccion.format("index.html"))