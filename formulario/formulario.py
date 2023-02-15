#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

#importamos las librerías
import cgi

#guardamos en args el valor dado
args = cgi.parse()

print("<b>Usuario: ", args['nombre'][0], "</b><br>")

print("<b>El número escogido es el: ", args['numero'][0], "</b><br><br>")

print(type(args))
print(type(args['numero']))
print(type(args['numero'][0]))

numero = int(args['numero'][0])

#if para delimitar el número entre el 1 y el 10
if 0 < numero < 11 :
    #bucle para hacer la tabla del número escogido
    for x in range (11):
        print("\t",numero," x ", x, " = ",x * numero,"<br>")
else:
    print("Debe de ser un número comprendido entre el 1 y el 10 contando estos")
