import numpy as np
import time
from algorithms.Core import *

def errorBreakPoints_dinamico(listaX,listaY,datos):
    errorTotal = 0
    
    for i in range(len(listaX) - 1):
        #elegimos 2 puntos a y b cada uno de estos tiene un punto (x,y) en la clave guardamos estos dos puntos (xa,ya),(xb,yb) con el error como valor de la clave
        clave = ((listaX[i], listaY[i]), (listaX[i+1], listaY[i+1]))
        
        #si la clave esta en el diccionario la devolvemos, sino se calcula y se guarda en el diccionario
        if clave in DiccionarioDeErrores:
            error_actual = DiccionarioDeErrores[clave]
        else:
            error_actual = errorAB(listaX[i], listaY[i], listaX[i+1], listaY[i+1], datos)
            DiccionarioDeErrores[clave] = error_actual
        errorTotal += error_actual
    
    return errorTotal
    

def pDinamicaV3(m:int,n:int,k:int, datos, dataName):
   
    start = time.time()
	
    #creamos la grilla en x y en y para los datos 
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    
    #sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    conjunto_medio:list = gridX[1:-1]

    # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    listas_medio = []
    listasCombinatorias(conjunto_medio,[],listas_medio,k-2)

    #agregamos el primer y ultimo elemento a cada lista 
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]

    bestRes = [gridY[-1]] * k
    bestError = float('inf')
    
     # Creo el diccionario (variable global) vacio
    global DiccionarioDeErrores
    DiccionarioDeErrores = {}

   
    
    #con cada subgrilla probamos pdinamicarecursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for subGridX in listas_medio:
        
        res = [gridY[0]] * len(subGridX)
        
        errorActual = 100000000000001
        
        errorActual = pDinamicaRecursiva(subGridX,gridY,[],[],res, errorActual, datos)
        
        #si otra subgrilla tiene un mejor error guarda esa 
        if(errorActual < bestError):
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()    
    
    end = time.time()

    totalTime = (end - start) * 1000
    
    #borramos el diccionario para que no se transfiera al llamar la funcion varias veces en el main 
    DiccionarioDeErrores.clear()

    plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"V3: Programacion Dinamica",bestError,totalTime,dataName)

    print("----PROG DINAMICAV3----")
    print(f"TIEMPO: {totalTime},\nFUNCION x: {bestSubGridX},\nFUNCION y: {bestRes},\nERROR: {bestError}\n\n")
    
    #devolvemos: mejor error, solucion en x, solucion en y y el tiempo total
    return np.round(bestError,decimals=2),bestSubGridX, bestRes,np.round(totalTime,decimals=2)



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