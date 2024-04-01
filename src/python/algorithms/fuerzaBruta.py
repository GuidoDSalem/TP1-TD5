import numpy as np
import time
import numpy as np
from algorithms.Core import *

def fuerzaBrutaRecursiva(gridX,gridY,xs:list,ys:list,res:list,datos):

    #Caso Base
    if(len(gridX)-1 == len(xs)):
        errorBP = errorBreakPoints(xs,ys,datos)
        return errorBP
    
    #Caso recursivo
    i = len(xs)
    bestError = 100000000
    mejorY = gridY[0]
    for j in gridY:
        xs.append(gridX[i+1])
        ys.append(j)
        error = fuerzaBrutaRecursiva(gridX,gridY,xs,ys,res,datos)
        xs.pop()
        ys.pop()
        if(error < bestError):
            bestError = error
            mejorY = j
    res.append(mejorY)

    print(f"Best Error: {bestError}")
    print(f"Res: {res}")
    return bestError


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

    bestError = fuerzaBrutaRecursiva(gridX,gridY,[],[],funcionYs,datos)

    end = time.time()

    totalTime = (end - start) * 1000

    return bestError,funcionYs,np.round(totalTime,decimals=2)