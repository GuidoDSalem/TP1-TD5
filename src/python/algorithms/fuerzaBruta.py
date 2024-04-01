import numpy as np
import time
import numpy as np
from algorithms.Core import *

def fuerzaBrutaRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):

    #Caso Base
    if(len(gridX) == len(xs)):
        print(f"XY: {ys}")
        errorBP = errorBreakPoints(xs,ys,datos)
        if(errorBP < bestError):
            bestError = errorBP
            res.clear()
            res.extend(ys)
            print(f"RES: {res},ERROR: {errorBP}")

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


    # errorTotal = 0
    # best_ys = []
    # for i in range(len(xs)-1):
    #     bestError = 1000000000000

    #     for ja in range(len(ys)):
    #         for jb in range(len(ys)):
    #             error = errorAB(xs[i],ys[ja],xs[i+1],ys[jb],datos)
    #             if(error < bestError):
    #                 bestError = error

    #     print(bestError)
    #     errorTotal += bestError



    return np.round(errorTotal,decimals=2)# bestError



def fuerzaBruta(Xs:int, Ys:int, datos):
    start = time.time()
	

    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=Xs, endpoint=True)

    funcionYs = []
    bestError = 1000000001

    bestError = fuerzaBrutaRecursiva(gridX,gridY,[],[],funcionYs,bestError,datos)

    end = time.time()

    totalTime = (end - start) * 1000

    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{funcionYs}\n")
    plot_puntos_y_linea(datos,gridX,funcionYs)

    return np.round(bestError,decimals=2),funcionYs,np.round(totalTime,decimals=2)