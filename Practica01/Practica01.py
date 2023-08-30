# Modulos
import os
import ast

def primerCadena(str1):
    registro = ''
    str1 = str1.split(':')
    for i in str1:
        aux = i.find('/')
        if(aux < 0):
            dec = str(int(i,base=16))
            registro = str(registro) + ':' + dec
        else:
            dec = str(int(i[:aux],base=16))
            registro = str(registro) + ':' + dec
    return registro

def tercerCadena(str1):
    registro = ''
    str1 = str1.split('.')
    for i in str1:
        aux = i.find('n')
        if(aux < 0):
            hexa = hex(int(i))
            aux2 = hexa.find('x') + 1
            registro = registro + '.' + hexa[aux2:]
        else:
            hexa = hex(int(i[:aux]))
            aux2 = hexa.find('x') + 1
            registro = registro + '.' + hexa[aux2:]
    return registro.upper()
    
    
    
data = open('prueba2.txt','r')
newdata = open('nuevo.txt','w')

contador = 1
for linea in data:
    cadena = linea.split(',')
    primero = primerCadena(cadena[0])
    segundo = cadena[2]
    tercero = tercerCadena(cadena[5])
    newdata.write(segundo + primero + tercero + os.linesep)
    contador += 1
data.close()
newdata.close()

