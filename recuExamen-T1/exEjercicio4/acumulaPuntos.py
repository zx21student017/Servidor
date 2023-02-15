#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

#importamos las librerías necesarias
import cgi,os
from http import cookies
import datetime

#creamos las variables que vayamos a necesitar
form = cgi.FieldStorage()
coki = cookies.SimpleCookie()

#si no hay caracteres en el input creamos una cookie de todas formas con valor vacio ""
if "puntos" in form:
    puntos = form['puntos'].value
else:
    puntos = "BORRAR"

if puntos == "BORRAR":

    #eliminamos la coki
    expires = datetime.datetime.utcnow() + datetime.timedelta(days=-1) #enviar cookie caducada
    coki['BORRAR']['expires'] = expires.strftime("%a, %d %b %Y %H:%M:%S GMT")
    print(coki)

else:
    #lista de todas las cookies
    todasCokis={}
    if'HTTP_COOKIE' in os.environ:
        listaCoki = os.environ['HTTP_COOKIE']
        listaCoki = listaCoki.split('; ') #para que sea correcto punto y coma con espacio
                                   
        for elemCoki in listaCoki:
            (nombre, valor) = elemCoki.split('=')
            todasCokis[nombre]=valor
    
    coki = cookies.SimpleCookie()
    todasCokis[nombre]=valor
    
print(coki)

print("Content-Type: text/html\n")

print(todasCokis)