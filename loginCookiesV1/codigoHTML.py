cabeceraHTML="""<html>
<head>
<title>{}</title>
<!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="http://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css">

  <!-- Latest compiled JavaScript -->
  <script src="http://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>

</head>
<body>
<h3>{}</h3>
"""

finHTML="""</body>
</html>
"""

#para volver a la página si no coinciden el login
redireccion = """
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Document</title>
    <meta http-equiv="Refresh" content="0; URL={}" />
</head>
<body>
</body>
</html>
"""