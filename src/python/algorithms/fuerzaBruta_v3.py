import numpy as np
import time
import numpy as np
from algorithms.Core import *


def fuerzaBrutaV3(m,n,k,datos):
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
        
    bestError = fuerzaBrutaRecursiva3(gridX,gridY,[],[],res,bestError,k,datos)



    end = time.time()

    totalTime = (end - start) * 1000



    plot_puntos_y_linea(datos,res[0],res[1],m,n,"FuerzaBrutaV3",bestError,totalTime)

    print(f"BEST XS: {res[1]},BEST YS: {error}, BEST ERROR: {bestError}")

    return np.round(bestError,decimals=2),res,np.round(totalTime,decimals=2)

def fuerzaBrutaRecursiva3(gridX:list,gridY:list,xs:list,ys:list,res:list,bestError:float,k:int, datos):
    BIG_NUMBER = 1000000001
    
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
                print(f"RES: {res[1]},ERROR: {error}")
                bestError = error
        
        return bestError

    # PASO RECURSIVO

    for i in range(len(gridX)):
        for j in range(len(gridY)):
            xs.append(gridX[i])
            ys.append(gridY[j])
            error = fuerzaBrutaRecursiva3(gridX,gridY,xs,ys,res,bestError,k-1,datos)
            if(error < bestError):
                bestError = error
            xs.pop()
            ys.pop()

    return bestError