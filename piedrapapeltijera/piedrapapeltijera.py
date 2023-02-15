#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/plain\n")

#importamos las librerías
import cgi
import random 

#guardamos en args el valor dado
args = cgi.parse()

jugadaHum = int(args['saca'][0])

#elegimos un objeto aleatorio para la máquina
jugadaMaq = random.randrange(1,4)

#mostramos resultado
if(jugadaHum == jugadaMaq):
	print("empate")
elif (jugadaHum == 1 and jugadaMaq == 2) or (jugadaHum == 2 and jugadaMaq == 3) or (jugadaHum == 3 and jugadaMaq == 1):
	print("Humano con : ", jugadaHum,"Maquina con: ", jugadaMaq," ¡gana la máquina!")
else :
	print("Humano con : ", jugadaHum,"Maquina con: ", jugadaMaq," ¡gana el humano!")
