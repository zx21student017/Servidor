#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

"""
crear un html con:
20)div -> img

div  id="contenedor1"
    img src="coche1.png" alt="imagen de coche 1"

div  id="contenedor2"
    img src="coche2.png" alt="imagen de coche 2"

etc...
"""

print("Content-Type: text/html\n")

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>Ejercicio-1</title>
    </head>
    <body>
""")

for n in range (1,21):
    print('<div id="contenedor'+str(n)+'">')

    print('     <img src="img/coche'+str(n)+'.png" alt="imagen de coche '+str(n)+'">')

    print('</div>')

print("""
    </body>
</html>
""")