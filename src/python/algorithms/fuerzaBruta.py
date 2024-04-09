import numpy as np
import time
import numpy as np
from algorithms.Core import *

def fuerzaBruta(m,n,k,datos):
    start = time.time()
	
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    print(f"\nGRID_X: {gridX}\nGRID_Y: {gridY}\n")
    
    conjunto_medio:list = gridX[1:-1]
    
    print(f"CONJ_MEDIO: {conjunto_medio}")
    

    listas_medio = []
    listasCombinatorias(conjunto_medio,[],listas_medio,k-2)

    print(f"\nLISTA_MEDIO: {listas_medio}\n\n")


    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]

    print(f"\nLISTA_MEDIO_COMPLETA: {listas_medio}\n\n")

    #######################################################################

    
    bestRes = []
    bestSubGridX =  [] 
    bestBestError = 100000000000001

    for i in range(k):
        bestRes.append(gridY[-1])
    
    for subGridX in listas_medio:
        print(subGridX)
        res = []
        for i in range(k):
            bestRes.append(gridY[-1])

        print(gridY.size)
        bestError = 100000000000001
        bestError = fuerzaBrutaRecursiva(subGridX,gridY,[],[],res, bestError, datos)
        if(bestError < bestBestError):
            bestSubGridX = subGridX.copy()
            bestBestError = bestError
            bestRes = res.copy()
    
    print(bestRes)
    end = time.time()

    totalTime = (end - start) * 1000

    # plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"FuerzaBurta",bestBestError,totalTime)

    # print(f"\nGridY: {gridY}")
    # print(f"\n\nTIEMPO: {totalTime}, FUNCION:{funcionYs}\n")
    

    return np.round(bestBestError,decimals=2),bestRes,np.round(totalTime,decimals=2)



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
