#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

import cgi
import mysql.connector

"""Para ver los errores bien gustosos
import cgitb

cgitb.enable()
print("Content-Type: text/html\n")
"""

form = cgi.FieldStorage()

#obtengo el nombre del socio, el titulo y el autor y compruebo si existe el parámetro
if "socio" in form and "titulo" in form and "autor" in form:
  socio = form['socio'].value
  titulo = form['titulo'].value
  autor = form['autor'].value

  #conectar a la base de datos
  mydb = mysql.connector.connect(
  host='localhost',
  user='biblioteca',
  password='biblioteca',
  database='biblioteca')

  mycursor = mydb.cursor()
  #seleccionamos el id según el nombre del socio que hayamos metido
  sql='SELECT id FROM socios where nombre = "'+socio+'"'
  mycursor.execute(sql)
  myresult=mycursor.fetchone()#guardamos el id de los socios que queremos
  
  #si existe el id, añade los valores, si no el socio no existe
  if mycursor.rowcount == 1:
    #guardamos el id (primer campo) del nombre que hayamos puesto
    ids = myresult[0]
    
    #insertamos dentro de la tabla libros el comentario que hayan realizado
    sql='INSERT INTO libros(titulo, autor, id_socio) VALUES(%s,%s,%s)' 
    val=(titulo,autor,ids)
    mycursor.execute(sql,val)
    mydb.commit()

    salida="Libro Prestado"
    
  else:
    salida="Socio no existe"

else:
  salida="Error. Falta un parámetro"

print("Content-Type: text/plain\n")
print(salida)