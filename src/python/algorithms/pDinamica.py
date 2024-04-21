import numpy as np
import time
from algorithms.Core import *

def pDinamica(m:int,n:int,k:int, datos, dataName:str):
   # Comenzamos a contar el tiempo de ejecucion
    start = time.time()
    
    #Sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=m)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=n)
     # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    conjunto_medio = gridX[1:-1]
    listas_medio = []
    listasCombinatorias(conjunto_medio, [], listas_medio, k-2)
    
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]
    
    bestRes = [gridY[-1]] * k
    bestError = float('inf')
    
    global DiccionarioDeErrores
    DiccionarioDeErrores = {}

    
    
    for subGridX in listas_medio:
        res = [gridY[0]] * len(subGridX)
        errorActual = pDinamicaRecursiva(subGridX, gridY, [], [], res, bestError, datos)
        
        if errorActual < bestError:
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()
        
        
    
    # Cortamos el tiempo y calculamos el tiempo de ejecucion
    end = time.time()
    totalTime = (end - start) * 1000

    # Generamos el grafico de la Instancia
    plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"V1: ProgramacionDinamica",bestError,totalTime,dataName)    

    return np.round(bestError,decimals=2),bestRes,np.round(totalTime,decimals=2)



def pDinamicaRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):

    #poda de optamalidad: si la rama que se esta calculando es mas grande que el mejor reusltado hasta ahora, descartala 
    errorActual = errorBreakPoints_dinamico(xs,ys,datos)
    if(errorActual > bestError):
        return bestError
    
    #Caso Base
    if(len(gridX) == len(xs)):
        
        if(errorActual < bestError):
            res.clear()
            res.extend(ys)

        return errorActual 
    
    if len(gridX) > len(xs):
        currentBestError = float('inf')
        for j in gridY:
            ys.append(j)
            error = pDinamicaRecursiva(gridX, gridY, xs + [gridX[len(xs)]], ys, res, bestError, datos)
            currentBestError = min(currentBestError, error)
            ys.pop()
        
        return currentBestError
    
    return bestError


def errorBreakPoints_dinamico(listaX, listaY, datos):
    errorTotal = 0
    for i in range(len(listaX) - 1):
        clave = ((listaX[i], listaY[i]), (listaX[i+1], listaY[i+1]))
        if clave in DiccionarioDeErrores:
            error_actual = DiccionarioDeErrores[clave]
        else:
            error_actual = errorAB(listaX[i], listaY[i], listaX[i+1], listaY[i+1], datos)
            DiccionarioDeErrores[clave] = error_actual
        errorTotal += error_actual
    return errorTotal
