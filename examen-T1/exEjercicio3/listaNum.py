#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

"""
Crear un diccionario de nombre preciosProductosID

Recorrer el diccionario para crear una tabla HTML
"""
import math

preciosProductosID = {
    "CA132":99.2,
    "CB231":55.7,
    "CA332":101.0,
    "CD563":65.2,
    "CB838":48.1
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
            <tr><th>identificador</th><th>precio</th></tr>
""")

total = 0

for elemento in preciosProductosID:
    print("<tr><td>"+elemento+"</td><td>"+str(preciosProductosID[elemento])+"</td></tr>")
    total += preciosProductosID[elemento]

print("<tr><td>Total</td><td>"+str(math.trunc(total))+"</td></tr>")

print("""
        </table>
    </body>
</html>
""")

"""
math.trunc(total) para truncar
round(total) para redondear
"""
