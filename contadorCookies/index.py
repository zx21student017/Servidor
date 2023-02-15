#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import codigoHTML
import os
from http import cookies

todasCookies={}
if 'HTTP_COOKIE' in os.environ:
    listaCoki = os.environ['HTTP_COOKIE'] #"contador=0;SID=ASDFasdf344"
    listaCoki = listaCoki.split('; ') #["contador=0","SID=ASDFasdf344"]
 
    for elemCoki in listaCoki:
        (nombre, valor) = elemCoki.split('=')
        todasCookies[nombre]=valor
 
    #todasCokis["contador"]="0"
    #todasCokis["SID"]="ASDFasdf344"
 
coki = cookies.SimpleCookie()
 
if 'contador' in todasCookies:
    coki["contador"]=int(todasCookies["contador"])+1
else:
    #esta parte solo se ejecuta la primera vez que accede el usuario
    coki["contador"]=1
   
print(coki)
 
print("Content-type: text/html\n")
 
print(codigoHTML.cabezeraHTML.format("Título", "contador de cookies"))
print(todasCookies)
print(codigoHTML.finHTML)
