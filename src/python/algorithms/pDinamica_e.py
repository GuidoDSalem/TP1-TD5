import numpy as np
import time
from algorithms.Core import *

def pDinamica(m, n, k, datos):
    #empiezo el tiempo
    start = time.time()
    
    #creo ambas subgrillas con m y n 
    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=m)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=n)
    
    #sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
    conjunto_medio = gridX[1:-1]
    
    # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    listas_medio = []
    listasCombinatorias(conjunto_medio, [], listas_medio, k-2)
    
     #agregamos el primer y ultimo elemento a cada lista  para tenr todas las subgrillas posibles
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]
    
    #inicializamos los peores casos posibles para todas las variables
    bestResY = [gridY[-1]] * k
    bestError = float('inf')
    errorActual = float('inf')
    bestResX = []
    
    #diccionario que va a guardar los puntos como claves y los errores como valores
    DiccionarioDeErrores = dict()
    
    #con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for subGridX in listas_medio:
        
        resY = [gridY[0]] * len(subGridX)
        
        errorActual = pDinamicaRecursiva(subGridX, gridY, [], [], resY, bestError, datos, DiccionarioDeErrores)
        
        if errorActual < bestError:
            bestResX = subGridX.copy()
            bestError = errorActual
            bestResY = resY.copy()
        
        
    #terminamos el tiempo 
    end = time.time()
    totalTime = (end - start) * 1000
    
    
    
    print("----Prog Dinamica----")

    print(f"\n\nTIEMPO: {totalTime}, FUNCIONx:{bestResX}, FUNCIONY:{bestResY},, ERROR:{bestError}\n")
    plot_puntos_y_linea(datos,bestResX,bestResY,m,n,"prog dinamica",bestError,totalTime)
    
    return np.round(bestError, decimals=2), bestResX, bestResY,np.round(totalTime, decimals=2)

def pDinamicaRecursiva(subGridX, gridY, xs, ys, resY, bestError, datos, DiccionarioDeErrores):
       
    #si la respuesta de error ya es mayor que la mejor respuesta (entera) devuelve infinito para que no trate ese camino devueelta
    if errorBreakPoints_dinamico(xs, ys, datos, DiccionarioDeErrores) > errorBreakPoints_dinamico(subGridX, resY, datos, DiccionarioDeErrores):
        return float('inf')
    
    #Caso Base
    if(len(subGridX) == len(xs)):
        
        #probamos el error con los puntos creados
        errorBP = errorBreakPoints_dinamico(xs, ys, datos, DiccionarioDeErrores)

        # y si es mejor que nuestra mejor solucion la cambiamos
        if(errorBP < bestError):
            resY.clear()
            resY.extend(ys)
            bestError = errorBP

        return bestError
    
    #Caso recursivo
    i = len(xs)
    xs.append(subGridX[i])
    currentBestError = bestError
    for j in gridY:
        ys.append(j)
        
        #calculamos el error con los datos que tengamos -> para poder guardar los puntos uno a uno y empezemos a llenar el diccionario con listas mas simples
        #esto va a generar que a medida que la lista se extendia no tnega que calcular toda la lista entera solo los ultimos puntos
        errorBreakPoints_dinamico(xs, ys, datos, DiccionarioDeErrores)
        
        error = pDinamicaRecursiva(subGridX,gridY,xs,ys,resY,currentBestError,datos, DiccionarioDeErrores)    

        #si la nueva funcion da un error mas chico cambiar el mejor error por eso
        if(error < currentBestError):
            currentBestError = error
            
        ys.pop()
    xs.pop()

    return currentBestError
   
   

def errorBreakPoints_dinamico(listaX, listaY, datos, diccionarioDeErrores):
    errorTotal = 0
    
    for i in range(len(listaX) - 1):
        clave = ((listaX[i], listaY[i]), (listaX[i+1], listaY[i+1]))
        if clave in diccionarioDeErrores:
            error_actual = diccionarioDeErrores[clave]
        else:
            error_actual = errorAB(listaX[i], listaY[i], listaX[i+1], listaY[i+1], datos)
            diccionarioDeErrores[clave] = error_actual
        errorTotal += error_actual
    
    return errorTotal

    