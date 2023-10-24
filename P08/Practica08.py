import random
import numpy as np
import time
from pynput import mouse

mouse_pressed = dict.fromkeys((mouse.Button.left, mouse.Button.right, mouse.Button.unknown), False)

def OnClick(x, y, button, pressed):
    mouse_pressed[button]=pressed

mouse.Listener(on_click=OnClick).start()
     
def agregarAuto():
    for i in range(len(estacionamiento)):
        if estacionamiento[i] == 1:
            estacionamiento[i] = 0
            break

def eliminarAuto():
    for i in range(len(estacionamiento)):
        if estacionamiento[i] == 0:
            estacionamiento[i] = 1
            break

def mostrarEstacionamiento():
    print('        |||||')
    for i in range(len(estacionamiento)):
        if estacionamiento[i] == 0:
            print('L', i+1, '\t| XX \n        |||||')
        else:
            #time.sleep(2)
            print('L', i+1, '\t|     \n        |||||')

if __name__ == '__main__':
    bandera = 0
    estacionamiento = [1,1,1,1,1,1,1,1,1,1,1,1]
    
    while True:
        time.sleep(1)
        if(mouse_pressed[mouse.Button.left]):
            print("boton izquierdo presionado")
            print('Entra auto<<<<<<<<<<<<<<<')
            if sum(estacionamiento) == 0:
                print('Lugar no disponible.')
            else:
                agregarAuto()
        if(mouse_pressed[mouse.Button.right]):
            print('Sale auto<<<<<<<<<<<<<<<<<')
            if sum(estacionamiento) == 12:
                print('No hay autos en el estacionamiento')
            else:
                eliminarAuto()
        acc = random.randrange(1,3,1)
        if acc == 1:
            print('Entra auto<<<<<<<<<<<<<<<')
            if sum(estacionamiento) == 0:
                print('Lugar no disponible.')
            else:
                agregarAuto()
        else:
            print('Sale auto<<<<<<<<<<<<<<<<<')
            if sum(estacionamiento) == 12:
                print('No hay autos en el estacionamiento')
            else:
                eliminarAuto()
        mostrarEstacionamiento()
        bandera += 1
        
    