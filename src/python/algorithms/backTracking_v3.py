import numpy as np
import time
import numpy as np
from algorithms.Core import *


def backTrackingV3(m,n,k,datos, dataName):
    start = time.time()
    #creamos la grilla en x y en y para los datos 
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)

    res = [[],[]]
        
    #esto lo hice porque la lista estba vacia para darles valores inciales porque 
    #sino en la priemra iteracion no podia iterar sobre valoers vacios por eso daba el lsit index out of range [1]
    for i in range(k):
        res[0].append(gridX[i])
        res[1].append(gridY[-1])

    

    bestError = 100000000000001
    currentError = 100000000000001

    bestError = backTrackingRecursivaV3(gridX,gridY,[],[],res,bestError,currentError,k,datos)



    end = time.time()

    totalTime = (end - start) * 1000



    plot_puntos_y_linea(datos,res[0],res[1],m,n,"V3:backTracking",bestError,totalTime, dataName)

    print("---BACK TRACKING V3----")
    print(f"TIEMPO: {totalTime},\nFUNCION x: {res[0]},\nFUNCION y: {res[1]},\nERROR: {bestError}\n\n")
    

    return np.round(bestError,decimals=2),res,np.round(totalTime,decimals=2)

def backTrackingRecursivaV3(gridX:list,gridY:list,xs:list,ys:list,res:list,bestError:float,currentError:float,k:int, datos):
    BIG_NUMBER = 1000000001

    # PODAS
    currentError = errorBreakPoints(xs,ys,datos)
    if(currentError > bestError):
        return BIG_NUMBER
    
    # CASO BASE
    if(k==0):
        # CASOS INFACTIBLES

        # no empieza en el principio del grid
        if xs[0] != gridX[0]:
            return BIG_NUMBER
        # no termina en el fin del grid
        if xs[-1] != gridX[-1]:
            return BIG_NUMBER
        # va para atras y/o arriba, o el mismo punto
        for i in range(k-1):
            if(xs[i] >= xs[i+1]):
                return BIG_NUMBER
        
        error = errorBreakPoints(xs,ys,datos)
        if(error < bestError):
                res[0].clear()
                res[1].clear()
                res[0].extend(xs)
                res[1].extend(ys)
                bestError = error
        
        return bestError

    # PASO RECURSIVO

    for i in range(len(xs),len(gridX)):
        xs.append(gridX[i])
        for j in range(len(gridY)):
            ys.append(gridY[j])
            error = backTrackingRecursivaV3(gridX,gridY,xs,ys,res,bestError,100000001,k-1,datos)
            if(error < bestError):
                bestError = error
            ys.pop()

        xs.pop()
    return bestError