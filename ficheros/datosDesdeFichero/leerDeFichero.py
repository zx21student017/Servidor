#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

from ast import For
import json

print("Content-Type: text/plain\n")

f = open("datos\listado.json","rt")

datosEnJson = json.loads(f.read())

f.close()
tam = len(datosEnJson)

for i in range(tam):
    print(i,":",datosEnJson[i])

for elemento in datosEnJson:
    print(elemento[0],"---",elemento[1])
