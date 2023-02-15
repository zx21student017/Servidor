#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

#importamos las librerías
import cgi

#guardamos en args el valor dado
args = cgi.parse()

texto = args['cadena'][0]

print(texto)

print(len(texto))#cuenta los caracteres

for letra in texto:#separa las letras
    print(letra)

if "hola" in texto:
    print("hola está en '"+texto+"'")

print(texto[4:8])
print(texto[:10])
print(texto[2:])

#palabra al revés
for letra in texto[::-1]:
    print(letra)