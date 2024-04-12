import numpy as np
import matplotlib.pyplot as plt
        
def error(m:float,x1,y1,xd,yd):
    """
    Dado una recta, calcula el error de un punto con la recta
    Returns: yPred = (m (xd - x1)) + y1 , m = (y2-y1)/(x2-x1)
    """
    
    yPred = m * (xd - x1) + y1
   
    return np.absolute(yPred - yd)


def pendiente(x1,y1,x2,y2):
    '''
    Dado dos puntos devuelve la pandiente de estos dos puntos 
    Returns: float
    '''
    
    try:
        m =  (y2-y1)/(x2-x1)
    except ZeroDivisionError:
        raise ValueError("Los dos puntos tienen la misma X -> No tiene pendiente!! ")
    return m
    

def errorAB(xa,ya,xb,yb,datos):
    """
    Dado un conjunto de datos, calcula el error de los datos que este entre A y B
    Pre: los datos deben estar ordenados

    Returns:
        float: _description_
    """
    
    # Caso que no es funcion pero es necesario... confia
    if(xa == xb):
        return 100000000

    m = pendiente(xa,ya,xb,yb)
    i = 0
    errorAcumulado = 0
    # Esto se podria reemplazar por una busqueda binaria para hacerlo mas eficiente
    if(datos["x"][0] > xb):
        return 0
    while  datos["x"][i] < xa:
        i+=1
    while(datos["x"][i] < xb):
       errorAcumulado += error(m,xa,ya,datos["x"][i],datos["y"][i])
       i+=1 

    return errorAcumulado


def errorBreakPoints(listaX,listaY,datos):
    '''
    Dado dos listas de puntos (uno para el eje x y otro para el eje y) y un dataset provisto devuelve el error total de todos los puntos preceidos menos los reales
    return: float
    '''
    errorTotal = 0
    for i in range(len(listaX) - 1):
        errorTotal += errorAB(listaX[i],listaY[i],listaX[i+1],listaY[i+1],datos)
    return errorTotal

def pepe():
    '''
    Funcion extremadamente importante que basicamente debuggeo todo el codigo
    pre: que corra python
    
    Returns: the truth
    '''
    return 3


def CrearMatriz(filas:int, columnas:int, valor_inicial:int):
    """
    Dada una cantidad de filas y columnas devuelvue una matriz de esas dnmensiones inicializada con valor inicial
    Pre: filas y columnas mas grande que 0 

    Returns:
        list: la matriz creada
    """
    
    matrix = np.full((filas, columnas), valor_inicial)
    return matrix

def plot_puntos_y_linea(data, linea_x, linea_y,m,n,algo,error,tiempo):
    """
    Grafica puntos y una línea basados en las coordenadas proporcionadas.

    :param puntos: Un diccionario con listas de coordenadas 'x' y 'y', y un contador 'n' de puntos.
    :param linea_x: Una lista de coordenadas 'x' para la línea.
    :param linea_y: Una lista de coordenadas 'y' para la línea.
    """
    
    # Graficar los puntos
    # Generar grilla de puntos usando numpy.linspace
    x_grilla = np.linspace(min(data['x']), max(data['x']), m)
    y_grilla = np.linspace(min(data['y']), max(data['y']), n)
    
    X, Y = np.meshgrid(x_grilla, y_grilla)

    # Graficar la grilla de puntos
    plt.scatter(X, Y, color='gray', s=2, label='Grilla')  # s es el tamaño de los puntos

    # Graficar los puntos
    plt.scatter(data['x'], data['y'], color='red', label='Puntos')

    # Graficar la línea
    plt.plot(linea_x, linea_y, color='blue', label='Línea')

    # Graficar puntos amarillos en los extremos de la línea
    plt.scatter(linea_x, linea_y, color='yellow',s=10, label='Puntos de Unión', zorder=5)

    # Añadir leyenda
    plt.legend()

    plt.title(f"{algo} Error: {np.round(error)},Tiempo:{np.round(tiempo,decimals=1)}  M:{m}, N:{n}")

    # Mostrar el gráfico
    plt.show()



def listasCombinatorias(lista:list,subconjuntos,lista_subconjuntos,k):
    '''
    Dado una lista de numeros y un int k particiona esa lista en subconjuntos de tamaño k 
    Return: modifica la lista_subconjuntos para dar todos los subconjuntos posibles 
    '''
    
    if(k==0):
        lista_subconjuntos.append(subconjuntos.copy())
        return
    if(len(lista) == 0):
        return 
    
    subconjuntos.append(lista[0])
    listasCombinatorias(lista[1:],subconjuntos,lista_subconjuntos,k-1)
    subconjuntos.pop()
    listasCombinatorias(lista[1:],subconjuntos,lista_subconjuntos,k)
