import numpy as np
import time
from algorithms.Core import *


def pDinamica(m, n, k, datos):
    start = time.time()
    
    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=m)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=n)
    
    conjunto_medio = gridX[1:-1]
    listas_medio = []
    listasCombinatorias(conjunto_medio, [], listas_medio, k-2)
    
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]
    
    bestRes = [gridY[-1]] * k
    bestError = float('inf')
    
    global DiccionarioDeErrores, memo
    DiccionarioDeErrores = {}
    memo = {}
    
    
    for subGridX in listas_medio:
        res = [gridY[0]] * len(subGridX)
        errorActual = pDinamicaRecursiva(subGridX, gridY, [], [], res, bestError, datos, memo)
        
        if errorActual < bestError:
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()
        
        
    
    end = time.time()
    totalTime = (end - start) * 1000
    
    print(memo)
    print(f"\nGridY: {gridY}")
    print(f"\n\nTIEMPO: {totalTime}, FUNCION:{bestRes}\n")
    
    return np.round(bestError, decimals=2), bestRes, np.round(totalTime, decimals=2)


def pDinamicaRecursiva(gridX, gridY, xs, ys, res, bestError, datos, memo):
    key = (tuple(xs), tuple(ys))
    
    if errorBreakPoints_dinamico(xs, ys, datos) > errorBreakPoints_dinamico(gridX, res, datos):
        return float('inf')
    
    if key in memo:
        if memo[key] == float('inf'):
            return float('inf')
        return memo[key]
    
    current_error = errorBreakPoints_dinamico(xs, ys, datos) if xs and ys else 0
    if current_error > bestError:
        memo[key] = float('inf')
        return float('inf')
    
    if len(gridX) == len(xs):
        errorBP = errorBreakPoints_dinamico(xs, ys, datos)
        memo[key] = errorBP
        if errorBP < bestError:
            res.clear()
            res.extend(ys)
            bestError = errorBP
        return errorBP
    
    if len(gridX) > len(xs):
        currentBestError = float('inf')
        for j in gridY:
            ys.append(j)
            error = pDinamicaRecursiva(gridX, gridY, xs + [gridX[len(xs)]], ys, res, bestError, datos, memo)
            currentBestError = min(currentBestError, error)
            ys.pop()
        memo[key] = currentBestError
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
