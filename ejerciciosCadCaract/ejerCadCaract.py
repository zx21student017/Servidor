#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

#importamos las librerías
import cgi

#guardamos en args el valor dado
args = cgi.parse()

texto = args['cadena'][0]

print("<b>Ejercicios de cadenas</b><br>")
print("===================== <br>")
print("Texto recibido: ",texto,"<br>")

#EJERCICIO 1
print("<hr>")
print("Ejercicio 1) <br>")
print("<br>")

contLetras = 0
for letra in texto:
    if (letra !=  " "):
        contLetras = contLetras + 1
print("Hay: ","<b>",contLetras,"</b>", "letras en la frase:","<b>", texto, "</b>")


#EJERCICIO 2
print("<hr>")
print("Ejercicio 2) <br>")
print("<br>")

palabraBuscar = args['palabra'][0]
print(palabraBuscar in texto)

#EJERCICIO 3
print("<hr>")
print("Ejercicio 3) <br>")
print("<br>")

letraBuscar = args['letra'][0]
contador = 0
###################POR ENTENDER########################
for letraBuscar in texto:
    i = contador + 1

print("Su letra ",letraBuscar,"aparece: ",i,"veces")

#EJERCICIO 4
print("<hr>")
print("Ejercicio 4) <br>")
print("<br>")

contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0

for letras in texto:
    if (letras == 'a'):
        contadorA = contadorA + 1
    elif(letras == 'e'):
        contadorE = contadorE + 1
    elif(letras == 'i'):
        contadorI = contadorI + 1
    elif(letras == 'o'):
        contadorO = contadorO + 1
    elif(letras == 'u'):
        contadorU = contadorU + 1
    
print("Tiene: <br>","a:",contadorA,"<br> e: ",contadorE,"<br> i: ",contadorI,"<br> o: ",contadorO,"<br> u: ",contadorU)

#EJERCICIO 5
print("<hr>")
print("Ejercicio 5) <br>")
print("<br>")

array = texto.split(' ')
a=1
for i in array:
     print (a,") ", i)
     #print (f" {a}) {i}")
     a=a+1

#EJERCICIO 6
print("<hr>")
print("Ejercicio 6) <br>")
print("<br>")

texto_reves = ""

#DAMOS LA VUELTA A CADA PALABRA
for letra in texto:
    texto_reves = letra + texto_reves

##################################

array = texto_reves.split(' ')

array_reves = ""

#DAMOS LA VUELTA AL ARRAY
for i in array:
     array_reves = i+ " " + array_reves

print(array_reves)