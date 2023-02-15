#!C:\Users\JJ\AppData\Local\Microsoft\WindowsApps\python.exe

"""
Crear una funcion de nombre concatenaVocales.

Recibe un parámetro con el nombre letras que es una lista(array).

comprobar:
    el tamaño sea 5 o menos

Devolver las letras concatenadas como un string
"""


def concatenaVocales(letras):
    
    salida=""

    if len(letras) > 5:#len(letras) para pasar la variable letras a entero
        return "error (más de 5 caracteres)"

    for lt in letras:
        if lt != 'A' and lt != 'E' and lt != 'I' and lt != 'O' and lt != 'U':
            return "error (caracter no encontrado)"
        salida += lt

    return salida

print("Content-Type: text/plain\n")

#pasamos a la funcion 'concatenaVocales' un valor para el parámetro 'letras'
print(concatenaVocales(['A','U'])) #AU
print("")
print(concatenaVocales(['b','U'])) #error (caracter no encontrado)
print("")
print(concatenaVocales(['A','U','E','O'])) #AUEO
print("")
print(concatenaVocales(['A','U','E','O','A','E','I'])) #error (más de 5 caracteres)