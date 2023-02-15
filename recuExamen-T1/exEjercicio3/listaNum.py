#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

import cgitb

MarcasCorredor = {
    '1001':["KIPRUTO, RHONEX",3469],
    '1002':["KIPLIMO, JACOB",3457],
    '1003':["KANDIE, KIBIWOTT",	3452],
    '1007':["MUTISO, ALEXANDER",3479],
    '1008':["WANDERS, JULIEN",3595],
    '1009':["KIPLIMO, PHILEMON",3491]
}

print("Content-Type: text/html\n")

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>Ejercicio-3</title>
    </head>
    <body>
        <table>
            <tr><th>dorsal</th><th>nombre</th></tr>
""")

ganador = "KANDIE, KIBIWOTT"

for dorsal in MarcasCorredor:
    print("<tr><td>"+dorsal+"</td><td>"+str(MarcasCorredor[dorsal][0])+"</td></tr>")
    

print("<tr><td>Ganador</td><td>"+str((ganador))+"</td></tr>")

print("""
        </table>
    </body>
</html>
""")
