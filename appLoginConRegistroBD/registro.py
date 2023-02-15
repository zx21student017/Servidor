#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi
import os.path
import codigoHTML
import sys
import hashlib
import mysql.connector

#conectar a base de datos
mydb = mysql.connector.connect(
    host='localhost',
    user='logReg',
    password='system',
    database='logReg'
)

mycursor = mydb.cursor()

datos = []

args = cgi.parse()


if "usuario" in args and "email" in args and "passwd" in args:
    datos.append(args["usuario"][0])
    datos.append(args["email"][0])
    
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    datos.append(h.hexdigest())
    
    correcto=True

    #vaciamos la tabla
    mycursor.execute("DELETE FROM tabla")

    #añadimos el admin
    mycursor.execute("INSERT INTO tabla (nombre, pass, correo, roll) VALUES (admin, admin, admin@correo.es, 1)")

    #añadimos valores a la tabla de los usuarios
    sql = 'INSERT INTO tabla (nombre, pass, correo, roll) VALUES (%s, %s, %s, 0)'

    for i in range(datos):
        #insertamos valores a la tabla
        valFila = (i[1],i[2],i[3],i[4])
        mycursor.execute(valFila)

    #para escribir en el log de error de apache
    for y in mycursor:
        for z in y:
            sys.stderr.write(">"+z+"<")    

    for x in mycursor:
        datosNombre = x[0]
        datosEmail = x[1]
        if datosNombre==datos[0] or datosEmail==datos[1]:
            print("Content-Type: text/html\n")
            print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Usuario ya existe. Redirigiendo","",""))
            print(codigoHTML.finalHTML)
            correcto=False
            break

    if correcto:
        
        print("Content-Type: text/html\n")

        print(codigoHTML.cabeceraHTML.format("Registro correcto",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Redirigiendo","",""))
        print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Faltan datos. Redirigiendo","",""))
    print(codigoHTML.finalHTML)