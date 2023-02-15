#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

#importamos las librerías
import cgi

#guardamos en args el valor dado
args = cgi.parse()

operacion = int(args['oper'][0])

numero1 = int(args['num1'][0])
numero2 = int(args['num2'][0])

if operacion == 1:
  print('El resultado de su suma es: ', numero1+numero2)
if operacion == 2:

  print('El resultado de su resta es: ', numero1-numero2)
if operacion == 3:

  print('El resultado de su multiplicación es: ', numero1*numero2)
if operacion == 4:

  print('El resultado de su división es: ', numero1/numero2)
if operacion < 1 or operacion > 4:

  print('error')