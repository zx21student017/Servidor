#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgi,os
import cgitb;cgitb.enable()

form = cgi.FieldStorage()

print("Content-Type: text/html\n")

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)

    open("img/"+fn,'wb').write(fileitem.file.read())

    print('<img src="img/'+fn+'">')