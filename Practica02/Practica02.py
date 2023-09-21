import os
import shutil
import random
import string

def cambiarCadena(st):
    print(st)
    newstring = ''
    for i in range(len(st)):
        if st[i].isdigit() == True:
            newstring = newstring + random.choice(string.ascii_letters)
        elif st[i].isalpha() == False:
            newstring = newstring + st[i]
        else:
            newstring = newstring + str(random.randint(0, 9))
    print(newstring)
    return(newstring.upper())
    

def Subcarpeta(folder,addres):                  # Funcion para subcarpetas
    os.chdir(os.path.join(addres, folder))      # Asignamos esta carpeta como principal
    newAddres = os.getcwd()                     # guardamos la direccion de la carpeta
    lista = os.listdir()                        # Listamos los elementos de la carpeta
    validarCarpeta(lista, newAddres)            # Llamamos de nuevo la funcion para evaluar carpeta
        


def validarCarpeta(lista, addres):              # Funcion evaluadora de archivos
    for file in lista:                          # Ciclo for para editar nombre
        os.rename(file, cambiarCadena(file))
        
    lista = os.listdir()                        # Actualizamos la lista con los nombres nuevos
    for file in lista:
        archivo = os.path.splitext(file)        # Variable de extension
        if archivo[1] == '':                    # Si no tiene extencion enviamos a evaluar la subcarpeta
            Subcarpeta(file,addres)                   # Si tiene solo pasamos
  
cadena = 'luis.14cruz@gmail.com'    
copy = 'Carpeta0001-copy'
direccion = os.getcwd()

if os.path.exists(copy) == True:
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
else:
    shutil.copytree('Carpeta0001', copy)

dirini = os.getcwd()
direccion = os.path.join(os.getcwd(), copy)     # Guardamos carpeta de trabajo principal
os.chdir(direccion)                             # Seleccionamos como carpeta de trabajo la copia
list = os.listdir()                             # Guardamos la lista de archivos


#cambiarCadena(cadena)
validarCarpeta(list, direccion)                 # Entramos a una funcion para evaluar datos de la carpeta
os.chdir(dirini)
