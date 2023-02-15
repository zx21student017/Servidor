#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

#importamos las librerías
import codigoHTML
from http import cookies
coki = cookies.SimpleCookie()
coki["contador"]=0
coki["jj"]="majo"
print(coki)

print("Content-Type: text/html\n")

#inicio del codigo HTML
print(codigoHTML.cabeceraHTML.format("Cookies","Cookies"))

#fin del codigo HTML
print(codigoHTML.finalHTML)