import numpy as np
import time

def fuerzaBrutaRecursiva(xs:list,ys:list,i,j):
    #Caso Base
    

    #Paso recursivo


    return np.random.randint(100)



def fuerzaBruta(Xs:int, Ys:int, datos):
    start = time.time()
	

    grid_x = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    grid_y = np.linspace(min(datos["y"]), max(datos["y"]), num=Xs, endpoint=True)



    bestError = fuerzaBrutaRecursiva(grid_x,grid_y,0,0)

    end = time.time()

    totalTime = int((end - start) * 1000)

    return bestError,np.random.randint(5,size=Xs),totalTime