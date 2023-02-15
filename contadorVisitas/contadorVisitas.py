#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

#importamos las librerías
import codigoHTML
import cgi

args = cgi.parse() #devuelve un diccionario

#iniciar el contador a 0 o al valor que viene desde la url
contadorLista = args.get("contador",[0])

contador=int(contadorLista[0])

contador=contador+1

#inicio del codigo HTML
print(codigoHTML.cabeceraHTML.format("Contador de visitas","Contador de visitas"))

print('<a href="contadorVisitas.py?contador='+str(contador)+'">llevas '+str(contador)+' visitas</a><br>')

print('<form action="contadorVisitas.py" method="post">')
print('<input type="texto" name="nomre">')
print('<input type="hidden" name="contador" value="'+str(contador)+'">')
print('<button type="submit">enviar</button>')
print('</form>')

#fin del codigo HTML
print(codigoHTML.finalHTML)