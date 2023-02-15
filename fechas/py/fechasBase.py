#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import datetime

###hora de ahorita mismo###
x = datetime.datetime.now()

print("Content-Type: text/plain\n")

fecha = x.strftime("%Y") +"-"+ x.strftime("%m") +"-"+ x.strftime("%d") +" "+ x.strftime("%H") +":"+ x.strftime("%M") +":"+ x.strftime("%S")

print("fecha exacta: ",fecha)
print()

print(type(x))
print("Fecha de ahora: ", x)
print()

print("Día num: ", x.day)
print("Día: ", x.strftime("%A"))
print("Día corto: ", x.strftime("%a"))

print("Mes num: ", x.month)
print("Mes escrito: ", x.strftime("%B"))
print("Mes corto: ", x.strftime("%b"))

print("Año: ", x.year)
print("Cuantos días llevamos de año: ",x.strftime("%j"))