#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import datetime
import cgi

datosForm = cgi.FieldStorage()

fecha = datosForm["fecha"].value if "fecha" in datosForm else False

print("Content-Type: text/plain\n")

if fecha :
    fecha = fecha.split("-")
    dFecha = datetime.datetime(int(fecha[0]),12,31)
    if int(dFecha.strftime("%j"))==366:
        print("Es bisiesto")
    else:
        print("No es biesiesto")
else:
    print("Error")