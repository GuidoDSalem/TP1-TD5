import numpy as np
import time
from Core import *

def fuerzaBrutaRecursiva(xs:list,ys:list,i,j,datos):
    #Caso Base
    if(i == len(xs)):
        return 0
    

    #Paso recursivo
    bestError = 10000000000
    for y in range(len(ys)):
        error = fuerzaBrutaRecursiva(xs,ys,i+1,y,datos)
        errorActual = errorAB(xs[i],ys[j],xs[i+1],y,datos)
        if(error + errorActual  < bestError):
            bestError = error + errorActual
    
    


    return np.random.randint(100)# bestError



def fuerzaBruta(Xs:int, Ys:int, datos):
    start = time.time()
	

    grid_x = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    grid_y = np.linspace(min(datos["y"]), max(datos["y"]), num=Xs, endpoint=True)



    bestError = fuerzaBrutaRecursiva(grid_x,grid_y,0,0)

    end = time.time()

    totalTime = int((end - start) * 1000)

    return bestError,np.random.randint(5,size=Xs),totalTime