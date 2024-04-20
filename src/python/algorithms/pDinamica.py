import numpy as np
import time
from algorithms.Core import *

def errorBreakPoints_dinamico(listaX,listaY,datos):
    errorTotal = 0
    error_actual = 0
    puntos = []
    for i in range(len(listaX) - 1):
        puntos.append((listaX[i],listaY[i]))
        puntos.append((listaX[i+1],listaY[i+1]))
        clave = (puntos[0],puntos[1])
        if (clave in DiccionarioDeErrores): # Si ya tengo el error entre estos dos puntos almacenado en mi diccionario, es decir ya lo calculé antes...
            error_actual = DiccionarioDeErrores[clave]
        else:
            error_actual = errorAB(listaX[i],listaY[i],listaX[i+1],listaY[i+1],datos)
            nueva_clave = clave
            DiccionarioDeErrores[nueva_clave] = error_actual # defino nueva clave en mi diccionario, una que no habia calculado antes
        errorTotal += error_actual
        puntos.clear()

    return errorTotal

def pDinamica(m:int,n:int,k:int, datos, dataName:str):
   
    start = time.time()
	
    #creamos la grilla en x y en y para los datos 
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    
    #sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    conjunto_medio:list = gridX[1:-1]

    # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    listas_medio = []
    listasCombinatorias(conjunto_medio,[],listas_medio,k-2)

    #agregamos el primer y ultimo elemento a cada lista 
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]

    bestRes = []
    bestSubGridX =  [] 
    bestError = 100000000000001

    # Creo la matriz (variable global) con -1's en todas sus posiciones
    global DiccionarioDeErrores
    DiccionarioDeErrores = dict()
   
    for i in range(k):
        bestRes.append(gridY[-1])
   
    
    #con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for subGridX in listas_medio:
        print(subGridX)
        res = []
       
        #esto lo hice porque la lista estba vacia para darles valores inciales porque 
        #sino en la priemra iteracion no podia iterar sobre valoers vacios por eso daba el lsit index out of range [1]
        for i in range(len(subGridX)):
            res.append(gridY[0])
        
        errorActual = 100000000000001
        
        errorActual = pDinamicaRecursiva(subGridX,gridY,[],[],res, errorActual, datos)
        
        #si otra subgrilla tiene un mejor error guarda esa 
        if(errorActual < bestError):
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()    
    
    end = time.time()

    totalTime = (end - start) * 1000


    plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"ProgramacionDinamica",bestError,totalTime,dataName)

    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{bestRes}\n")
    

    return np.round(bestError,decimals=2),bestRes,np.round(totalTime,decimals=2)



def pDinamicaRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):

    #poda de optamalidad: si la rama que se esta calculando es mas grande que el mejor reusltado hasta ahora, descartala 
    errorActual = errorBreakPoints_dinamico(xs,ys,datos)
    if(errorActual > bestError):
        return bestError
    
    #Caso Base
    if(len(gridX) == len(xs)):
        
        # errorBP = errorBreakPoints_dinamico(xs,ys,datos)
            
        # errorActual = errorBreakPoints_dinamico(xs,res,datos)
        
        # print(f"XY: {ys}, Error: {np.round(errorBP,decimals=2)}")
        if(errorActual < bestError):
            # bestError = errorBP
            res.clear()
            res.extend(ys)


        return errorActual 
    
    #Caso recursivo
    i = len(xs)
    xs.append(gridX[i])
    currentBestError = bestError
    for j in gridY:
        ys.append(j)
        error = pDinamicaRecursiva(gridX,gridY,xs,ys,res,currentBestError,datos)
        # m[posicion] = error
        if(error < currentBestError):
            currentBestError = error
        ys.pop()
    xs.pop()

    return currentBestError