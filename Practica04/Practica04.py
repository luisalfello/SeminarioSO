# Modulos
import os
import time


def round(new, ordenados):
    n = 0
    for i in range(len(new)):
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
        
def agregarProceso(process):
    newProcess = []
    print('Introduce nombre de proceso:')
    newProcess.append(input())
    
    print('Introduce Tiempo de ejecucion:')
    newProcess.append(input())
    
    print('Introduce prioridad:')
    newProcess.append(input())
    
    print('En que posicion desea agregar el proceso:')
    print(' 1. Principio')
    print(' 2. Final')
    pos = input()
    process.append(newProcess)
    if pos == '2':
        n = len(process) - 1
        for i in range(len(process)-1):
            t = process[n]
            process[n] = process[n-1] 
            process[n-1] = t
            n = n - 1
        
def menuAlgoritmosPlanificacion(process):
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
            SJF(process)
        elif opc == 2:
            FIFO(process)
        elif opc == 3:
            Prioridades(process)
        elif opc == 4:
            roundRobin(process)
        else:
            break

def menuProcesos(process):
    opc = 0
    while opc != int:
        print('------Algoritmos de planificación------')
        print(' 1. Mostrar procesos')
        print(' 2. Agregar procesos')
        print(' 3. Algorimos de planificación')
        print(' 4. Salir')
        print('Seleccione: ')
        opc = int(input())
        
        if opc == 1:
            #os.system("cls")
            for i in range(len(process)):
                priori = process[i][2].replace('\n', '')
                print('Proceso: ', process[i][0],'\t\t\t Tiempo: ',process[i][1],'\tPrioridad: ',priori)
        elif opc == 2:
            agregarProceso(process)
            #print(process)
        elif opc == 3:
            menuAlgoritmosPlanificacion(process)
        else:
            break        
    
if __name__ == '__main__':
    data = open('procesos.txt','r')
    procesos = []
    for linea in data:
        aux = linea.split(',')
        aux = [elem.replace(' ','') for elem in aux]
        procesos.append(aux)
        
    menuProcesos(procesos)
    
    data.close()