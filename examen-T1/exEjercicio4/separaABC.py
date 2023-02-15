#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

#importamos las librerías necesarias
import cgi,os
from http import cookies

#creamos las variables que vayamos a necesitar
form = cgi.FieldStorage()
coki = cookies.SimpleCookie()

#si no hay caracteres en el input creamos una cookie de todas formas con valor vacio ""
if "texto" in form:
    palabra = form['texto'].value
else:
    palabra = ""

if palabra == "":

    coki["empiezaABC"]=""
    coki["otras"]=""

#creamos las cookies según los caracteres que nos manden
else:
    #lista de todas las cookies
    todasCokis={}
    if'HTTP_COOKIE' in os.environ:
        listaCoki = os.environ['HTTP_COOKIE']
        listaCoki = listaCoki.split('; ') #para que sea correcto punto y coma con espacio
                                   
        for elemCoki in listaCoki:
            (nombre, valor) = elemCoki.split('=')
            todasCokis[nombre]=valor

    abc=""
    noAbc=""
    
    if(palabra[0]=="A" and palabra[1]=="B" and palabra[2]=="C"):
        abc=palabra
    else:
        noAbc=palabra

    if 'empiezaABC' in todasCokis:
        coki['empiezaABC']=todasCokis['empiezaABC'] + " " + abc
    else:
        coki['empiezaABC']=abc

    if 'otras' in todasCokis:
        coki['otras']=todasCokis['otras'] + " " + noAbc
    else:
        coki['otras']=noAbc

print(coki)

print("Content-Type: text/html\n")

print(todasCokis)

"""
#guardamos en args el valor dado
args = cgi.parse()
texto = args['texto'][0]

empiezanABC = cookies.SimpleCookie()
otras = cookies.SimpleCookie()

if texto[0:3] == "ABC":

    #creamos las cookies que empiezan por ABC
    empiezanABC["empiezanABC"]=texto

    print(empiezanABC)

elif texto[0:3] != "ABC":
    #creamos las cookies que no empiezan por ABC
    
    otras["otras"]=texto

    print(otras)

elif texto == "":
    otras["otras"]=""
    empiezanABC["empiezanABC"]=""

    print(empiezanABC)
    print(otras)

    print("Content-Type: text/html\n")

    print("<b>Texto vacio.</b><br>")


#################################################
print("Content-Type: text/html\n")

print("<b>Texto: ", args['texto'][0], "</b><br>")
"""