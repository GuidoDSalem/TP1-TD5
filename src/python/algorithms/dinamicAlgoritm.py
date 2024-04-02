import numpy as np
import time
import numpy as np
from algorithms.Core import *

def dinamicAlgoritm(Xs:int, Ys:int, datos):
    print("ENTRE1")

    start = time.time()

    gridX = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    gridY = np.linspace(min(datos["y"]), max(datos["y"]), num=Ys, endpoint=True)

    # PRIMER TRAMO
    bestError = 100000000
    # function = [gridY[-1],gridY[-1]] # Por default
    function = np.zeros(len(gridX))
    print(f"Function: {function}")

    for ya in gridY:
        for yb in gridY:
            error = errorAB(gridX[0],ya,gridX[1],yb,datos)
            if(error < bestError):
                bestError = error
                function[0] = ya
                function[1] = yb
    # Fin del Primer Tramo
    print("ENTRE2")

    # El resto de la funcion

    for i in range(1,len(gridX)-1):
        
        bestErrorTramo = 1000000000
        for yb in gridY:
            error = errorAB(gridX[i],function[i],gridX[i+1],yb,datos)
            if(error < bestErrorTramo):
                print("ENTRE 4")
                bestErrorTramo = error
                function[i+1] = yb
        bestError += bestErrorTramo

    # fin del resto de la funcion
    
    

    end = time.time()

    plot_puntos_y_linea(datos,gridX,function,Xs,Ys)
    totalTime = (end - start) * 1000

    return np.round(bestError,decimals=2),function,np.round(totalTime,decimals=2)



    