import numpy as np
import time
import numpy as np
from algorithms.Core import *

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


def fuerzaBruta(Xs:int, Ys:int,k_breakpoints:int, datos):
    start = time.time()
	

    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=Ys, endpoint=True)

    coordenadas:list = generar_coordenadas(gridX,gridY)

    funcionYs = []
    for i in range(len(gridX)):
        funcionYs.append(gridY[-1])
    bestError = 1000000001

    bestError = fuerzaBrutaRecursiva(gridX,gridY,[],[],funcionYs,bestError,datos)

    end = time.time()

    totalTime = (end - start) * 1000

    plot_puntos_y_linea(datos,gridX,funcionYs,Xs,Ys,"FuerzaBurta",bestError,totalTime)

    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{funcionYs}\n")
    

    return np.round(bestError,decimals=2),funcionYs,np.round(totalTime,decimals=2)


def fuerzaBrutaRecursiva2(coordenadas:list,list_temp:list,res:list,bestError,k_breakpoints:int,datos):
    print(f"RES: {res}")
    print(f"TEMP: {res}")
    #Caso Base
    if(len(coordenadas) == 0):
        return 0
    
    if(k_breakpoints == 0):
        errorBP = errorCoordenadas(list_temp,datos)
        errorActual = errorCoordenadas(res,datos)

        if(errorBP < errorActual):
            # bestError = errorBP
            res.clear()
            res.extend(list_temp)
            print(f"RES: {res},ERROR: {errorBP}")
            bestError = errorBP
        return bestError

    
    #Caso recursivo
    list_temp.append(coordenadas[0])
    error_a = fuerzaBrutaRecursiva2(coordenadas[1:],list_temp,res,bestError,k_breakpoints-1,datos)
    list_temp.pop()

    error_b = fuerzaBrutaRecursiva2(coordenadas[1:],list_temp,res,bestError,k_breakpoints,datos)

    if(error_a <= error_b):
        
        return error_a
    else:
        return error_b

    # fuerzaBrutaRecursiva2(coordenadas:list,list_temp:list,ys:list,res:list,bestError,k_breakpoints:int,datos)

    return 0

def fuerzaBruta2(Xs:int, Ys:int,k_breakpoints:int, datos):
    start = time.time()
	

    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=Ys, endpoint=True)

    coordenadas:list = generar_coordenadas(gridX,gridY)

    res = []
    for i in range(len(gridX)):
        res.append([gridX[i],gridY[-1]])
    bestError = 1000000001

    bestError = fuerzaBrutaRecursiva2(coordenadas,[],res,bestError,k_breakpoints,datos)

    end = time.time()

    totalTime = (end - start) * 1000

    plot_coordenadas_y_linea(datos,res,Xs,Ys,"FuerzaBurta",bestError,totalTime)

    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{res}\n")
    

    return np.round(bestError,decimals=2),res,np.round(totalTime,decimals=2)