import os

def tamArchivo():
    tArchivo = []
    for i in range(len(archivos)):
        aux = archivos[i][1]
        tArchivo.append(int(aux))
    return tArchivo

def tMemoria(m):
    memoria = []
    for i in m:
        memoria.append(i)
    print(memoria)
    return memoria
    

def primerAjuste():
    memoria = tMemoria(m)
    len(memoria)
    tArchivo = tamArchivo()

    for i in range(len(archivos)):
        bandera = 0
        for j in range(len(memoria)):
            if tArchivo[i] <= memoria[j]:
                memoria[j] = memoria[j] - tArchivo[i]
                aux = archivos[i][0]
                print('file',i,':',aux[:11], '\tPeso:',tArchivo[i],'\tLote:',j,'\tDisponible:', memoria[j])
                bandera = 0
                break
            elif tArchivo[i] > memoria[j]:
                bandera = 1
        if bandera == 1:
            aux = archivos[i][0]
            print('file',i,':', aux[:11], '\tPeso:',tArchivo[i], ' No cabe en memoria')
    print(memoria)
            

def mejorAjuste():
    memoria = tMemoria(m)
    tArchivo = tamArchivo()
    
    for i in range(len(archivos)):
        bandera = 0
        mejor = 100000
        imem = 0
        for j in range(len(memoria)):
            if tArchivo[i] <= memoria[j]:
                temp = memoria[j] - tArchivo[i]
                bandera += 1
                if temp < mejor and temp >= 0:
                    mejor = temp
                    imem = j
            #elif tArchivo[i] > memoria[i]:
            #    bandera = 1
        if bandera >= 1:
            memoria[imem] = memoria[imem] - tArchivo[i]
            aux = archivos[i][0]
            print('file',i,':',aux[:11], '\tPeso:',tArchivo[i],'\tLote:',imem,'\tDisponible:', memoria[imem])
        if bandera == 0:
            aux = archivos[i][0]
            print('file',i,':', aux[:11], '\tPeso:',tArchivo[i], ' No cabe en memoria')
    print(memoria)

            
def peorAjuste():
    memoria = tMemoria(m)
    tArchivo = tamArchivo()
    
    for i in range(len(archivos)):
        bandera = 0
        mejor = 0
        imem = 0
        for j in range(len(memoria)):
            if tArchivo[i] <= memoria[j]:
                temp = memoria[j] - tArchivo[i]
                bandera = 0
                if temp >= mejor and temp >= 0:
                    mejor = temp
                    imem = j
            elif tArchivo[i] > memoria[imem]:
                bandera = 1
        if bandera == 0:
            memoria[imem] = memoria[imem] - tArchivo[i]
            aux = archivos[i][0]
            print('file',i,':',aux[:10], '\tPeso:',tArchivo[i],'\tLote:',imem,'\tDisponible:', memoria[imem])
        if bandera == 1:
            aux = archivos[i][0]
            print('file',i,':', aux[:11], '\tPeso:',tArchivo[i], ' No cabe en memoria')
    print(memoria)


def siguienteAjuste():
    memoria = tMemoria(m)
    tArchivo = tamArchivo()

    imem = 0
    for i in range(len(archivos)):
        bandera = 0
        for j in range(len(memoria)):
            j = imem
            if tArchivo[i] <= memoria[j]:
                memoria[j] = memoria[j] - tArchivo[i]
                aux = archivos[i][0]
                print('file',i,':',aux[:10], '\tPeso:',tArchivo[i],'\tLote:',j,'\tDisponible:', memoria[j])
                bandera = 0
                imem = j
                break
            elif tArchivo[i] > memoria[j]:
                if imem+1 < len(memoria):
                    imem += 1
                bandera = 1
        if bandera == 1:
            aux = archivos[i][0]
            print('file',i,':', aux[:11], '\tPeso:',tArchivo[i], ' No cabe en memoria')
    print(memoria)

def agregarArchivos():
    newFile = []
    print('Introduce el nombre del archivo:')
    newFile.append(input())
    
    print('Introduce el peso del archivo en kb:')
    newFile.append(input())
    
    print('En que posicion desea agregar el espacio:')
    print(' 1. Principio')
    print(' 2. Final')
    pos = input()
    archivos.append(newFile)
    if pos == '1':
        n = len(archivos) - 1 
        for i in range(len(archivos)-1):
            t = archivos[n]
            archivos[n] = archivos[n-1] 
            archivos[n-1] = t
            n = n - 1

def agregarMemoria():
    print('Introduce cantidad de memoria en kb:')
    newMemory = (int(input()))
    
    print('En que posicion desea agregar el espacio:')
    print(' 1. Principio')
    print(' 2. Final')
    pos = input()
    m.append(newMemory)
    if pos == '1':
        n = len(m) - 1 
        for i in range(len(m)-1):
            t = m[n]
            m[n] = m[n-1] 
            m[n-1] = t
            n = n - 1

def menuMemoryAdmin():
    opc = 0
    while opc != int:
        print('-------------------------------------')
        print('---Administración de Memoria---')
        print(' 1. Primer ajuste')
        print(' 2. Mejor ajuste')
        print(' 3. Peor ajuste')
        print(' 4. Siguiente ajuste')
        print(' 5. Salir')
        opc = int(input())
        if opc == 1:
            print('----------Primer Ajuste----------')
            primerAjuste()
        elif opc == 2:
            print('----------Mejor Ajuste----------')
            mejorAjuste()
        elif opc == 3:
            print('----------Peor Ajuste----------')
            peorAjuste()
        elif opc == 4:
            print('----------Siguiente Ajuste----------')
            siguienteAjuste()
        else:
            break
    

def menuPrincipal():
    opc = 0
    while opc != int:
        print('-------------------------------------')
        print('---Practica 06---')
        print(' 1. Mostrar bLoques de memoria')
        print(' 2. Mostrar archivos y pesos')
        print(' 3. Agregar memoria')
        print(' 4. Agregar archivos')
        print(' 5. Algoritmos de admin de memoria ')
        print(' 6. Salir')
        opc = int(input())
        if opc == 1:
            print('----------Memoria----------')
            for i in range(len(m)):
                print('Bloque',i,':',m[i],'kb')
        elif opc == 2:
            
            print('----------Archivos----------')
            for i in range(len(archivos)):
                aux = archivos[i][0]
                print('file',i,':',aux[:10], '\tPeso:',archivos[i][1],'kb')
        elif opc == 3:
            print('----------Agregar memoria----------')
            agregarMemoria()
        elif opc == 4:
            print('----------Agregar archivos----------')
            agregarArchivos()
        elif opc == 5:
            print('----------Algoritmos de admin de memoria----------')
            menuMemoryAdmin()
        else:
            break

if __name__ == '__main__':
    #data = open('archivos.txt','r')
    archivos = []
    
    #for linea in data:
        #archivos.append(linea.split())
        
    direccion = os.path.join(os.getcwd(), 'archivos') 
    os.chdir(direccion)
    files = os.listdir()
    m = [1000,400,1800,700,900,1200,1500]
    for i in range(len(files)):
        aux = files[i],str(round(os.stat(files[i]).st_size/1000))
        archivos.append(aux)
    #print(archivos)
    
    menuPrincipal()
    #mejorAjuste()
    
