#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi
import mysql.connector
import json

#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='ventacamiones',
  password='ventacamiones',
  database='ventacamiones'
)

mycursor = mydb.cursor()

#obtengo la imagen, el titulo y el comentario
form = cgi.FieldStorage()
marca = form['marca'].value
modelo = form['modelo'].value
precio = form['precio'].value
desc = form['desc'].value

resultado = True

sql="INSERT INTO camiones (marca,modelo,precio,descripcion,fechaCreacion) VALUES (%s,%s,%s,%s,now())"
val = (marca, modelo, precio, desc)
mycursor.execute(sql, val)

mydb.commit()

print("Content-Type: text/plain\n")
print(json.dumps(resultado))
