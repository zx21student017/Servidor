#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi
import codigoHTML
import hashlib
import mysql.connector
import datetime

#conectar a la base de datos
mydb = mysql.connector.connect(
  host='localhost',
  user='comentaLibros',
  password='comentaLibros',
  database='comentaLibros'
)

args = cgi.parse()


if "usuario" in args and "email" in args and "passwd" in args:
    user = args["usuario"][0]
    mail = args["email"][0]
    
    h=hashlib.sha512(str.encode(args["passwd"][0]))
    passwd=h.hexdigest()

    #creamos la fecha que se une el usuario
    x = datetime.datetime.now()
    fecha = x.strftime("%Y") +"-"+ x.strftime("%m") +"-"+ x.strftime("%d") +" "+ x.strftime("%H") +":"+ x.strftime("%M") +":"+ x.strftime("%S")

    #crear un cursor a la base de datos
    mycursor = mydb.cursor()

    #buscar el usuario en base de datos

    sql = 'SELECT COUNT(*) FROM usuarios where usuario like \"%s\"'

    val=(user,)

    mycursor.execute(sql,val)

    myresult = mycursor.fetchone()

    if myresult[0]==0:
        #inserta en base de datos
        sql = 'INSERT INTO usuarios (usuario, passwd, mail, fecha, rolid) VALUES (%s, %s, %s, %s, 2)'

        val = (user, passwd, mail, fecha)
        mycursor.execute(sql, val)

        mydb.commit()

        print("Content-Type: text/html\n")
        print(codigoHTML.cabeceraHTML.format("Registro correcto",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Redirigiendo","",""))
        print(codigoHTML.finalHTML)
    else:    
        print("Content-Type: text/html\n")
        print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Ya existe el usuario. Redirigiendo","",""))
        print(codigoHTML.finalHTML)
else:
    print("Content-Type: text/html\n")
    print(codigoHTML.cabeceraHTML.format("Fallo en el registro",'<meta http-equiv="Refresh" content="2; URL=index.html"/>',"Faltan datos. Redirigiendo","",""))
    print(codigoHTML.finalHTML)