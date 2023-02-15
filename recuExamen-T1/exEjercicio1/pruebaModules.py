#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

print("Content-Type: text/html\n")

print("""
<!DOCTYPE html>
<html>
    <head>
        <title>Ejercicio-1</title>
    </head>
    <body>
""")

for n in range (1,11):

    print('<a href="producto'+str(n)+'.html" title="Ir al produto '+str(n)+'">Producto número '+str(n)+'</a>')

print("""
    </body>
</html>
""")