import numpy as np
import time
import numpy as np
from algorithms.Core import *


def backTrackingRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):

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
        error = backTrackingRecursiva(gridX,gridY,xs,ys,res,currentBestError,datos)
        if(error < currentBestError):
            currentBestError = error
        ys.pop()
    xs.pop()

    return currentBestError


def backTracking(Xs:int, Ys:int, datos):
    start = time.time()
	

    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=Ys, endpoint=True)

    funcionYs = []
    for i in range(len(gridX)):
        funcionYs.append(gridY[-1])
    bestError = 1000000001

    bestError = fuerzaBrutaRecursiva(gridX,gridY,[],[],funcionYs,bestError,datos)

    end = time.time()

    totalTime = (end - start) * 1000

    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{funcionYs}\n")
    plot_puntos_y_linea(datos,gridX,funcionYs,Xs,Ys)

    return np.round(bestError,decimals=2),funcionYs,np.round(totalTime,decimals=2)