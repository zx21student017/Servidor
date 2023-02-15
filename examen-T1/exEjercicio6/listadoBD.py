#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

import mysql.connector

#conectar a base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='biblioteca',
    password='biblioteca',
    database='biblioteca')

mycursor = mydb.cursor()
#seleccionamos todas las filas de la tabla socio
sql = "SELECT * FROM socios"
mycursor.execute(sql)
myresult = mycursor.fetchall()#guardamos todos los casos del conjunto de datos de la tabla de socios

print("Content-Type: text/html\n")

print('<html><head><meta charset="UTF-8"></head><body>')
print('<h2>Listado de libros prestados</h2>')

#hacemos un bucle para guardar cada uno de los socios en filas como socio1 con su id de la tabla de socios
for socio in myresult:
    ids=socio[0]
    nombre=socio[1]
    
    sql='SELECT titulo FROM libros where id_socio='+str(ids)
    mycursor.execute(sql)
    myresultLibros = mycursor.fetchall()

    if mycursor.rowcount > 0:
        print('<hr>')
        print('<h3>'+nombre+' Ha recibido un prestamo </h3>')

        #hacemos un bucle para sacar cada una de las líneas de la tabla libros
        for libro in myresultLibros:
            print('<p>'+libro[0]+'</p>')
    
    else: 
        print('<h3>'+nombre+'No tiene ningun prestamo </h3>')