import numpy as np
import time
import numpy as np
from algorithms.Core import *

def fuerzaBrutaDinamicaRecursiva(gridX,gridY,xs:list,ys:list,res:list,mat_res,bestError,datos):
    
    
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
    indexJ = 0
    for j in gridY:
        ys.append(j)
        # Caso hay valor en mar_res
        if(mat_res[i-1][indexJ] != -1):
            return mat_res[i-1][indexJ][0]
        else:
            error = fuerzaBrutaDinamicaRecursiva(gridX,gridY,xs,ys,res,mat_res,currentBestError,datos)
            mat_res[i-1][indexJ] = (error,ys)
            indexJ += 1
            if(error < currentBestError):
                currentBestError = error
            ys.pop()
    xs.pop()

    return currentBestError


def dinamicAlgoritm(Xs:int, Ys:int, datos):

    start = time.time()

    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=Ys, endpoint=True)

    matriz_res = np.zeros(shape=[Xs,Ys]) - 1
    print(matriz_res)


    funcionYs = []
    # for i in range(len(gridX)):
    #     funcionYs.append(gridY[-1])
    bestError = 1000000001

    bestError = fuerzaBrutaDinamicaRecursiva(gridX,gridY,[],[],funcionYs,matriz_res,bestError,datos)

    end = time.time()

    totalTime = (end - start) * 1000
    bestError = 42

    plot_puntos_y_linea(datos,gridX,function,Xs,Ys,"Dinamico",bestError,totalTime)

    return np.round(bestError,decimals=2),function,np.round(totalTime,decimals=2)



    