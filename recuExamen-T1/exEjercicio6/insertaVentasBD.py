#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi
import mysql.connector
import math

form = cgi.FieldStorage()

#obtengo el nombre del dni, el adultos y el menores y compruebo si existe el parámetro
if "dni" in form and "adultos" in form and "menores" in form:
  dni = form['dni'].value
  adultos = int(form['adultos'].value)
  menores = int(form['menores'].value)

  #conectar a la base de datos
  mydb = mysql.connector.connect(
  host='localhost',
  user='museo',
  password='museo',
  database='museo')

  mycursor = mydb.cursor()
  #seleccionamos el id según el dni del comprador que hayamos metido
  sql='SELECT id FROM comprador where dni = "'+dni+'"'
  mycursor.execute(sql)
  myresult=mycursor.fetchone()
  
  #si existe el id, añade los valores, si no el comprador no existe
  if mycursor.rowcount == 1:
    
    ids = myresult[0]

    total = round((adultos * 20)+(menores * 5),2)
    
    
    #insertamos dentro de la tabla entradas las compras que hayan realizado
    sql='INSERT INTO entradas(numAdultos, numMenores, id_comprador, total) VALUES(%s,%s,%s,%s)' 
    val=(adultos,menores,ids,total)
    mycursor.execute(sql,val)
    mydb.commit()

    salida="Compra realizada"
  
  #si no, el comprador no existe
  else:
    salida="Comprador no existe"

#si no, falta un parametro
else:
  salida="Error. Falta un parámetro"

print("Content-Type: text/plain\n")
print(salida)