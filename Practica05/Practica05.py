def tamArchivo():
    tArchivo = []
    for i in range(len(archivos)):
        aux = archivos[i][1]
        index = aux.find('k')
        aux = aux[:index]
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
                print('file',i,':',aux[:10], '\tPeso:',tArchivo[i],'\tLote:',j,'\tDisponible:', memoria[j])
                bandera = 0
                break
            elif tArchivo[i] > memoria[j]:
                bandera = 1
        if bandera == 1:
            aux = archivos[i][0]
            print('file',i,':', aux[:10], ' No cabe en memoria')
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
                bandera = 0
                if temp < mejor and temp >= 0:
                    mejor = temp
                    imem = j
            elif tArchivo[i] > memoria[i]:
                bandera = 1
        if bandera == 0:
            memoria[imem] = memoria[imem] - tArchivo[i]
            aux = archivos[i][0]
            print('file',i,':',aux[:10], '\tPeso:',tArchivo[i],'\tLote:',imem,'\tDisponible:', memoria[imem])
        if bandera == 1:
            aux = archivos[i][0]
            print('file',i,':', aux[:10], ' No cabe en memoria')
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
            print('file',i,':', aux[:10], '\tPeso:',tArchivo[i], ' No cabe en memoria')
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
            print('file',i,':', aux[:10], ' No cabe en memoria')
    print(memoria)


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
    

if __name__ == '__main__':
    data = open('archivos.txt','r')
    archivos = []
    m = [1000,400,1800,700,900,1200,1500]
    for linea in data:
        archivos.append(linea.split())
    menuMemoryAdmin()
