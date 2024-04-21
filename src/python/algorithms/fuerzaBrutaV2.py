import numpy as np
import time
import numpy as np
from algorithms.Core import *

def fuerzaBruta(m,n,k,datos,dataName:str):
    #Comenzamos a tomar el tiempo de ejecuciom
    start = time.time()
	
    #creamos la grilla en x y en y para los datos 
    gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
    gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    
    #sacamos el primer y ultimo elemento de la grilla x para trabajar unicamente con las columnas del medio
    conjunto_medio:list = gridX[1:-1]

    # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
    listas_medio = []
    listasCombinatorias(conjunto_medio,[],listas_medio,k-2)

    #agregamos el primer y ultimo elemento a cada lista 
    listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]


    bestRes = []
    bestSubGridX =  [] 
    bestError = 100000000000001

    # Agregamos datos por default
    for i in range(k):
        bestRes.append(gridY[-1])
    
    
    #con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
    for subGridX in listas_medio:
        # print(subGridX)
        res = []
        
        #esto lo hice porque la lista estba vacia para darles valores inciales porque 
        #sino en la priemra iteracion no podia iterar sobre valoers vacios por eso daba el lsit index out of range [1]
        for i in range(len(subGridX)):
            res.append(gridY[0])
        
        errorActual = 100000000000001
        
        errorActual = fuerzaBrutaRecursiva(subGridX,gridY,[],[],res, errorActual, datos)
        
        #si otra subgrilla tiene un mejor error guarda esa 
        if(errorActual < bestError):
            bestSubGridX = subGridX.copy()
            bestError = errorActual
            bestRes = res.copy()    
    
    # Detenemos el tiempo y calculamos el tiempo de ejecucion
    end = time.time()
    totalTime = (end - start) * 1000

    # Generamos el Grafico de esta Instancia
    plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"FuerzaBruta",bestError,totalTime,dataName)

    return np.round(bestError,decimals=2),bestRes,np.round(totalTime,decimals=2)



def fuerzaBrutaRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):
    
    #Caso Base
    if(len(gridX) == len(xs)):
        
        errorActual = errorBreakPoints(xs,ys,datos)
        
        if(errorActual < bestError):
            res.clear()
            res.extend(ys)
            bestError = errorActual

        return bestError
    
    #Caso recursivo
    i = len(xs)
    xs.append(gridX[i])

    for j in gridY:
        ys.append(j)
        error = fuerzaBrutaRecursiva(gridX,gridY,xs,ys,res,bestError,datos)
        if(error < bestError):
            bestError = error
        ys.pop()
    xs.pop()

    return bestError