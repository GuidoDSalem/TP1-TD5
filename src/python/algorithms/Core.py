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
    yPred = (m (xd - x1)) + y1 , m = (y2-y1)/(x2-x1)
    """
    yPred = m * (xd - x1) + y1
    return np.absolute(yPred - yd)


def pendiente(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

def errorAB(xa,ya,xb,yb,datos):
    m = (yb - ya)/(xb - xa)
    i = 0
    errorAcumulado = 0

    while(xa < datos[i].x  and datos[i].x < xb):
        errorAcumulado += error(m,xa,ya,datos[i].x,datos[i].y)
        i+=1
    return errorAcumulado

