import numpy as np
import time
import numpy as np
from algorithms.Core import *


def fuerzaBruta(m,n,k,datos,dataName:str):
    #Comenzamos a tomar el tiempo de ejecuciom
    start = time.time()
    #creamos la grilla en x y en y para los datos 
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    
    #sacamos el primer y ultimo elemento de la grilla x para trabajar unicamente con las columnas del medio
    conjunto_medio:list = gridX[1:-1]

    # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    listas_medio = []
    listasCombinatorias(conjunto_medio,[],listas_medio,k-2)

    #agregamos el primer y ultimo elemento a cada lista 
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]

    bestRes = []
    bestSubGridX =  [] 
    bestError = 100000000000001

    for i in range(k):
        res[0].append(gridX[i])
        res[1].append(gridY[-1])

        bestError = float('inf')
            
        errorActual = 100000000000001
            
        errorActual = fuerzaBrutaRecursiva(subGridX,gridY,[],[],res, errorActual, datos)
            
        #si otra subgrilla tiene un mejor error guarda esa 
        if(errorActual < bestError):
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()    
    
    end = time.time()
    totalTime = (end - start) * 1000


    plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"Back Tracking",bestError,totalTime)

    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{bestRes}\n")
    

    return np.round(bestError,decimals=2),bestRes,np.round(totalTime,decimals=2)



def fuerzaBrutaRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):
    
    #Caso Base
    if(len(gridX) == len(xs)):
        
        errorBP = errorBreakPoints(xs,ys,datos)
        
        errorActual = errorBreakPoints(xs,res,datos)
        
        # print(f"XY: {ys}, Error: {np.round(errorBP,decimals=2)}")
        if(errorBP < errorActual):
            # bestError = errorBP
            res.clear()
            res.extend(ys)
            print(f"RES: {res},ERROR: {errorBP}")
            bestError = errorBP

        return bestError
    
    #Caso recursivo
    i = len(xs)
    xs.append(gridX[i])
    currentBestError = bestError
    for j in gridY:
        ys.append(j)
        error = fuerzaBrutaRecursiva(gridX,gridY,xs,ys,res,currentBestError,datos)
        if(error < currentBestError):
            currentBestError = error
        ys.pop()
    xs.pop()

    return currentBestError
