#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import mysql.connector

#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='museo',
  password='museo',
  database='museo')

mycursor = mydb.cursor()
#seleccionamos todas las filas de la tabla comprador
mycursor.execute("SELECT * FROM comprador")
myresult = mycursor.fetchall()#guardamos todos los casos del conjunto de datos de la tabla de comprador

print("Content-Type: text/html\n")

print('<html><head><meta charset="UTF-8"></head><body>')
print('<h2>Entradas Vendidas</h2>')

#hacemos un bucle para guardar cada uno de los compradores 
for comprador in myresult:
    
    mycursor.execute("SELECT * FROM entradas where id_comprador="+str(comprador[0]))
    myresultEntradas = mycursor.fetchall()
    
    print('<hr>')
    print('<h3>'+str(comprador[1])+' ha comprado las siguientes: </h3>')

    #hacemos un bucle para sacar cada una de las líneas de la tabla entradas
    for entrada in myresultEntradas:
        print('<p>'+str(entrada[1])+' de adulto y '+str(entrada[2])+' de ninio por '+str(entrada[3])+'euros</p>')

    