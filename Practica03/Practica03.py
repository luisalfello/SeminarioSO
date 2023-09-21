# Modulos
import os
import time


def round(new, ordenados):
    n = 0
    for i in range(10):
        contador = 0
        for j in range(new[n]):
            if contador == 3:
                break
            elif new[n] != 0:
                print('TIEMPO: ',new[n],' PROCESO: ',ordenados[n][0],'...',)
                new[n] -= 1
                time.sleep(.1)
                contador += 1
        n += 1
    print(new)
    return sum(new)
    
    
    
def SJF(process):
    print('SJF(El mas corto primero)')
    ordenados = sorted(process, key=lambda corto : int(corto[1]))
    print(ordenados)
    n = 0
    for i in ordenados:
        temporizador = int(i[1])
        for j in range(temporizador):
            print('TIEMPO: ',temporizador,' PROCESO: ',ordenados[n][0],'...',)
            temporizador -= 1
            time.sleep(.1)
        n += 1


def FIFO(process):
    print('FIFO(El primero en llegar, el primero en salir)')
    n = 0
    for i in process:
        temporizador = int(i[1])
        for j in range(temporizador):
            print('TIEMPO: ',temporizador,' PROCESO: ',process[n][0],'...',)
            temporizador -= 1
            time.sleep(.1)
        n += 1

def Prioridades(process):
    print(' 3. Prioridades')
    ordenados = sorted(process, key=lambda corto : int(corto[2]))
    print(ordenados)
    #n = len(ordenados) - 1
    n = 0
    for i in ordenados:
        temporizador = int(i[1])
        for j in range(temporizador):
            print('TIEMPO: ',temporizador,' PROCESO: ',ordenados[n][0],'...',)
            temporizador += 1
            #temporizador -= 1
            time.sleep(.1)
        n += 1
        #n -= 1

def roundRobin(process):
    print(' 4. Round Robin')
    new = []
    ordenados = sorted(procesos, key=lambda corto : int(corto[1]))
    for i in ordenados:
        new.append(int(i[1]))
    
    num = 1
    while num != 0:
        num = round(new,ordenados)
        
    
                


            
data = open('procesos.txt','r')
procesos = []
for linea in data:
    aux = linea.split(',')
    aux = [elem.replace(' ','') for elem in aux]
    procesos.append(aux)
#SJF(procesos)
#FIFO(procesos)
#Prioridades(procesos)
#roundRobin(procesos)
opc = 0
while opc != int:
    print('------Algoritmos de planificacion------')
    print(' 1. SJF(El mas corto primero)')
    print(' 2. FIFO(El primero en llegar, el primero en salir)')
    print(' 3. Prioridades')
    print(' 4. Round Robin')
    print(' 5. Salir u otra tecla')
    print('Seleccione: ')
    opc = int(input())

    if opc == 1:
        SJF(procesos)
    elif opc == 2:
        FIFO(procesos)
    elif opc == 3:
        Prioridades(procesos)
    elif opc == 4:
        roundRobin(procesos)
    else:
        break




procesos.close()