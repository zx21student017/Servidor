codigoHTML="""
<!DOCTYPE html>
<html lang="es">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="Refresh" content="{}, URL={}"/>
</head>

<body>
  <h1>{}</h1>
</body>
</html>
"""

redireccion = lambda r,s,t : print(codigoHTML,format(r,s,t))

def redReg ():
    redireccion(2,"aplicacion.html","Registro Completado")
def redLog ():
    redireccion(2,"pagina1.py","Login Completado")
def redLogError ():
    redireccion(2,"aplicacion.html","Datos no coincidentes")
