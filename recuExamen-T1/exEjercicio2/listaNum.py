#!C:\Users\zx21student017\AppData\Local\Microsoft\WindowsApps\python

def cuentaNumeros(frase):
    
    salida=0
    if len(frase) > 100:
        return "error (más de 100 caracteres)"

    for c in frase:
        if (c=='0') or (c=='1') or (c=='2') or (c=='3') or (c=='4') or (c=='5') or (c=='6') or (c=='7') or (c=='8') or (c=='9'):
            salida+=1 
    return salida
        

print("Content-Type: text/plain\n")

#pasamos a la funcion 'cuentaNumeros' un valor para el parámetro 'frase'
print(cuentaNumeros("hola 123")) #devuelve 3
print("")
print(cuentaNumeros("En un lugar de la Mancha")) #devuelve 0
print("")
print(cuentaNumeros("699 766 987")) #devuelve 9
print("")
print(cuentaNumeros("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) #devuelve "error (más de 100 caracteres)"


#if lt != 'A' and lt != 'E' and lt != 'I' and lt != 'O' and lt != 'U':
#            return "error (caracter no encontrado)"
#        salida += lt
#
#    return salida