import numpy as np
import time
from algorithms.Core import *

def backTracking(m:int,n:int,k:int, datos): # O(2^n × n^2 × m^2)
   
    start = time.time()
	
    #creamos la grilla en x y en y para los datos 
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    
    #sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    conjunto_medio:list = gridX[1:-1]

    # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    listas_medio = []
    listasCombinatorias(conjunto_medio,[],listas_medio,k-2) #O(2^n) donde n = len(conjunto_medio) = len(gridx) -2 

    #agregamos el primer y ultimo elemento a cada lista 
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]
    
    #solucion en y
    bestRes = []
    #solucion en x
    bestSubGridX =  [] 
    bestError = float('inf')

    for i in range(k):
        bestRes.append(gridY[-1])
    
    #con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for subGridX in listas_medio:
        res = []
       
        #esto lo hice porque la lista estba vacia para darles valores inciales porque 
        #sino en la priemra iteracion no podia iterar sobre valoers vacios por eso daba el lsit index out of range [1]
        for i in range(len(subGridX)):
            res.append(gridY[0])
        
        errorActual = float('inf')
        
        errorActual = backTrackingRecursiva(subGridX,gridY,[],[],res, errorActual, datos) # O(n^2×m^2) # n = len(subgridX) m = cantidad máxima de datos entre dos puntos consecutivos en subgridX
        
        #si otra subgrilla tiene un mejor error guarda esa 
        if(errorActual < bestError):
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()    
    
    end = time.time()

    totalTime = (end - start) * 1000


    #plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"BackTracking",bestError,totalTime)
    
    print("----BACK TRACKING----")
    print(f"TIEMPO: {totalTime},\nFUNCION x: {bestSubGridX},\nFUNCION y: {bestRes},\nERROR: {bestError}\n\n")
    
    #devolvemos: mejor error, solucion en x, solucion en y y el tiempo total
    return np.round(bestError,decimals=2),bestSubGridX, bestRes,np.round(totalTime,decimals=2)



def backTrackingRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):
    # poda de optamilidad: si la rama que se esta calculando es mas grande que el mejor reusltado hasta ahora, descartala 
    if(errorBreakPoints(xs,ys,datos) > errorBreakPoints(gridX,res,datos)):
        return errorBreakPoints(xs,ys,datos)
    
    #Caso Base
    if(len(gridX) == len(xs)):
        
        errorBP = errorBreakPoints(xs,ys,datos)
        
        errorActual = errorBreakPoints(xs,res,datos) 
        
        if(errorBP < errorActual):
            res.clear()
            res.extend(ys)
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
