import numpy as np

def calculateFunctionError(breakPoints:list,data)->float:
    """
    Dado una lista de puntos que son los que une y define a la funcion que estamos diseniando
    calcula el error de las predicciones de los datos para esa funcion

    Pre: Los datos estan ordenados segun la variable x, para todo i en BP: breakPoints[0].x <data[i].x < breakPoints[-1].x, |breakPoints| >= 2
    Post: -
    """
    i = 0
    errorAcumulado = 0
    m = pendiente(breakPoints[i].x,breakPoints[i].y,breakPoints[i+1].x,breakPoints[i+1].y)
    for dataX,dataY in data:

        while not ((breakPoints[i] < dataX) and (dataX <= breakPoints[i+1])):

            i += 1
            m = pendiente(breakPoints[i].x,breakPoints[i].y,breakPoints[i+1].x,breakPoints[i+1].y)

        errorAcumulado += error(m,breakPoints[i],breakPoints[i+1],dataX,dataY)
    
    return errorAcumulado
        
def error(m,x1,y1,xd,yd):
    
    """
    Dado una recta, calcula el error de un punto con la recta
    yPred = (m (xd - x1)) + y1 , m = (y2-y1)/(x2-x1)
    """
    yPred = m * (xd - x1) + y1
    print(f"|Ypred - Y| = |{yPred} - {yd}| = {np.absolute(yPred - yd)}")
    return np.absolute(yPred - yd)


def pendiente(x1,y1,x2,y2):
    try:
        m =  (y2-y1)/(x2-x1)
    except ZeroDivisionError:
        print(x2,x1)
        raise ValueError("Los dos puntos tienen la misma X -> No tiene pendiente!! ")
    return m
    

def errorAB(xa,ya,xb,yb,datos):
    
    """
    Dado un conjunto de datos, calcula el error de los datos que este entre A y B
    Pre: los datos deben estar ordenados

    Returns:
        float: _description_
    """

    m = pendiente(xa,ya,xb,yb)
    i = 0
    errorAcumulado = 0
    # Esto se podria reemplazar por una busqueda binaria para hacerlo mas eficiente
    while  datos["x"][i] < xa:
        i+=1
    print(i)
    while(datos["x"][i] < xb):
       errorAcumulado += error(m,xa,ya,datos["x"][i],datos["y"][i])
       i+=1 

    return errorAcumulado

