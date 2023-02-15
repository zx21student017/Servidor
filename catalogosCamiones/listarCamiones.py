#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

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
 
#consultar en la base de datos la lista de todos los camiones
sql="SELECT marca,modelo,descripcion,precio,imagen, DATE_FORMAT(fechaCreacion, '%Y-%m-%d %T') FROM camiones ORDER BY fechaCreacion DESC"
mycursor.execute(sql)
lc = mycursor.fetchall()
print("Content-Type: text/html\n")
print(json.dumps(lc))

