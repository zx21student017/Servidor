#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

import cgi
from socket import inet_aton

args = cgi.parse()

####TÍTULO#####
print("<h3>Figuritas Tochas >:)</h3>")

#####declaramos las variables de las figura. http://www.servidor.es/figuras/tareaFiguras.py?nfilas=5&figura=1####
nfilas = int(args["nfilas"][0])
figura = int(args["figura"][0])
caracter = '* '

#### función para guardar las letras del abecedario
def llenarAbecedario():
     abecedario = []
     for i in range(65, 91):
          abecedario.append(chr(i))
     return abecedario

abecedario = llenarAbecedario()

#### funcion figura 1
def figura1(nf, c):
    print("Figura 1.")
    print("")

    linea = ""

    for i in range(nf):
          for j in range(nf-i-1):
               linea += ' '
          for j in range(i+1):
               linea += c
          print(linea)
          linea = ''
     
    nf -= 1
    for i in range(nf):
          for j in range(i+1):
               linea += ' '
          for j in range(nf-i):
               linea += c
          print(linea)
          linea = ''

#### funcion figura 2
def figura2(nf):
    print("Figura 2.")
    print("")

    linea = ""
    contador = 1

    for i in range(nf):
          for k in range(nf-i-1):
               linea += " "
          for j in range(i+1):
               linea += str(contador) + " "
          contador += 1
          print(linea)
          linea = ''
     
    nf -= 1
    contador -= 2
    for i in range(nf):
          for k in range(i+1):
               linea += ' '
          for j in range(nf-i):
               linea += str(contador) + ' '
          contador -= 1
          print(linea)
          linea = ''

#### funcion figura 3
def figura3(nf):
    print("Figura 3.")
    print("")

    linea = ""
    contador = 1

    for i in range(nf):
          for k in range(nf-i-1):
               linea += ' '
          for j in range(i+1):
               linea += str(contador, abecedario)+' '
          contador += 1
          print(linea)
          linea = ''

    nf -= 1
    contador -= 2
    for i in range(nf):
          for k in range(i+1):
               linea += ' '
          for j in range(nf-i):
               linea += str(contador, abecedario) + ' '
          contador -= 1
          print(linea)
          linea = ''

###MENÚ FIGURAS###
match figura:
    case 1:
        figura1(nfilas)
    case 2:
        figura2(nfilas)
    case 3:
        figura3(nfilas)
    case _:
        print("opcion ni completada")