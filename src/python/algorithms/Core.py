import numpy as np
import matplotlib.pyplot as plt

######################################################funciones auxiliares   
     
def error(m,x1,y1,xd,yd):
    
    """
    Dado una recta, calcula el error de un punto con la recta
    yPred = (m (xd - x1)) + y1 , m = (y2-y1)/(x2-x1)
    """
    yPred = m * (xd - x1) + y1
    # print(f"|Ypred - Y| = |{yPred} - {yd}| = {np.absolute(yPred - yd)}")

    
    return np.absolute(yPred - yd)

def pendiente(x1,y1,x2,y2):
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
    while(datos["x"][i] <= xb):
       
       errorAcumulado += error(m,xa,ya,datos["x"][i],datos["y"][i])
       i+=1 
       if( i == len(datos["x"])):
           return errorAcumulado
            

    return errorAcumulado

def errorBreakPoints(listaX,listaY,datos):
    errorTotal = 0
    for i in range(len(listaX) - 1):
        errorTotal += errorAB(listaX[i],listaY[i],listaX[i+1],listaY[i+1],datos)
    return errorTotal

def listasCombinatorias(lista:list,subconjuntos,lista_subconjuntos,k):
    if(k==0):
        lista_subconjuntos.append(subconjuntos.copy())
        return
    if(len(lista) == 0):
        return 
    
    subconjuntos.append(lista[0])
    listasCombinatorias(lista[1:],subconjuntos,lista_subconjuntos,k-1)
    subconjuntos.pop()
    listasCombinatorias(lista[1:],subconjuntos,lista_subconjuntos,k)
    
def pepe():
    return 3

#######################################################funciones para graficar
def plot_puntos_y_linea_sin_save(data, linea_x, linea_y,m,n,algo,error,tiempo):
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

    plt.title(f"{algo}")
    plt.text(0.5, -0.10, f"Error: {np.round(error)}     Tiempo: {np.round(tiempo,decimals=1)}     Grilla: [{m},{n}]", ha='center', va='center', transform=plt.gca().transAxes, fontsize=8)

    # Mostrar el gráfico
    plt.show()

def plot_puntos_y_linea(data, linea_x, linea_y,m,n,algo,error,tiempo,dataName):
    """
    Grafica puntos y una línea basados en las coordenadas proporcionadas.

    :param puntos: Un diccionario con listas de coordenadas 'x' y 'y', y un contador 'n' de puntos.
    :param linea_x: Una lista de coordenadas 'x' para la línea.
    :param linea_y: Una lista de coordenadas 'y' para la línea.
    """
    # dataName = "firulais"
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

    plt.title(f"{algo}")
    plt.text(0.5, -0.10, f"Error: {np.round(error)}     Tiempo: {np.round(tiempo,decimals=1)}     Grilla: [{m},{n}]", ha='center', va='center', transform=plt.gca().transAxes, fontsize=8)

    fileName = f"{algo}_{m}x{n}_{len(linea_x)}"

    plt.savefig(f"./src/python/graficos/{dataName[:-5]}/" + fileName)

    plt.close()

    # Mostrar el gráfico
    # plt.show()
  
def comparacion_tiempo(tiempos_list, algorithm_names, breakpoints_lists, avg_t, instance, dataName, i, j):
   
    plt.figure(figsize=(10, 6))
   
    
    # Plot errors vs breakpoints for each algorithm
    for time, breakpoints, algorithm_name in zip(tiempos_list, breakpoints_lists, algorithm_names):
        plt.plot(breakpoints, time, label=algorithm_name)

    plt.xlabel('Breakpoints')
    plt.ylabel('Time')
    plt.title(f'Time vs Breakpoints en: {dataName}')
    plt.legend()
    plt.text(0.5, -0.13, f"Diferencia de tiempo en promedio: {avg_t}         Grilla: [{i},{j}]", ha='center', va='center', transform=plt.gca().transAxes, fontsize=8)
    plt.grid(True)
    
    fileName = f"Tiempo vs Breakpoints {dataName[:-5]}_{i}x{j}"

    plt.savefig(f"./src/python/graficos/tiempos/{dataName[:-5]}" + fileName)

    plt.close()
    
    #plt.show()
    
def comparacion_errores(errores_list, breakpoints_lists, instance, dataName, i, j):
   
    plt.figure(figsize=(10, 6))
   
    
    # Plot errors vs breakpoints for each algorithm
    
    plt.plot(breakpoints_lists, errores_list)

    plt.xlabel('Breakpoints')
    plt.ylabel('Error')
    plt.title(f'Error vs Breakpoints en: {dataName}')
    plt.legend()
    plt.text(0.5, -0.13, f"Grilla: [{i},{j}]     Numero de puntos: {instance["n"]}", ha='center', va='center', transform=plt.gca().transAxes, fontsize=8)
    plt.grid(True)
    
    fileName = f"Error vs Breakpoints {dataName[:-5]}_{i}x{j}"

    plt.savefig(f"./src/python/graficos/errores/{dataName[:-5]}" + fileName)

    plt.close()
    
    #plt.show()
       
def comparacion_tiempos_dataset(tiempos_fuerza_bruta,tiempos_backtracking,tiempos_pdinamic,datasets):
    n = len(datasets)  # Número de datasets
    r = np.arange(n)  # Array con la posición de cada dataset
    width = 0.25       # Ancho de las barras

    # Crear el gráfico de barras
    plt.figure(figsize=(10, 5))  # Tamaño del gráfico

    # Barras para fuerza bruta
    plt.bar(r, tiempos_fuerza_bruta, color = 'g', width = width, edgecolor = 'grey', label='Fuerza Bruta')

    # Barras para backtracking
    plt.bar(r + width, tiempos_backtracking, color = 'b', width = width, edgecolor = 'grey', label='Backtracking')

    # Barras para programación dinámica
    plt.bar(r + 2 * width, tiempos_pdinamic, color = 'r', width = width, edgecolor = 'grey', label='Programación Dinámica')

    # Añadir títulos y etiquetas
    plt.xlabel('Datasets', fontweight ='bold', fontsize = 15)
    plt.ylabel('Tiempo de ejecución', fontweight ='bold', fontsize = 15)
    plt.xticks(r + width, datasets)

    # Añadir leyenda
    plt.legend()

    #mostrar grafico 
    plt.show()



    
#################### no las usamos ###############################################
def print_dict(dictionary):
    print("{")
    for key, value in dictionary.items():
        print(f"    '{key}': '{value}',")
    print("}")

def initialize_dictionary(gridX, gridY):
    dictionary = {}
    for xa in gridX:
        for ya in gridY:
            for xb in gridX:
                for yb in gridY:
                    dictionary[(xa, ya), (xb, yb)] = None
    return dictionary

def generar_coordenadas(gridX, gridY):
    # Usar una comprensión de lista para generar todas las combinaciones posibles
    todas_las_coordenadas = [(x, y) for x in gridX for y in gridY]
    return todas_las_coordenadas

def errorCoordenadas(coordenadas,datos):
    errorTotal = 0
    for i in range(len(coordenadas) - 1):
        errorTotal += errorAB(coordenadas[i][0],coordenadas[i][1],coordenadas[i+1][0],coordenadas[i+1][1],datos)
    return 0

def generar_coordenadas(gridX, gridY):
    # Usar una comprensión de lista para generar todas las combinaciones posibles
    todas_las_coordenadas = [(x, y) for x in gridX for y in gridY]
    return todas_las_coordenadas

def CrearMatriz(filas, columnas, valor_inicial):
    """
    Dada una cantidad de filas y columnas devuelvue una matriz de esas dnmensiones inicializada con valor inicial
    Pre: filas y columnas mas grande que 0 

    Returns:
        list: la matriz creada
    """
    
    matrix = np.full((filas, columnas), valor_inicial)
    return matrix

def plot_coordenadas(linea_x,linea_y,puntos, coordenadas,m,n):
    """
    Grafica puntos y una línea basados en las coordenadas proporcionadas.

    :param puntos: Un diccionario con listas de coordenadas 'x' y 'y', y un contador 'n' de puntos.
    :param linea_x: Una lista de coordenadas 'x' para la línea.
    :param linea_y: Una lista de coordenadas 'y' para la línea.
    """
    
    # Graficar los puntos
    # Generar grilla de puntos usando numpy.linspace
    x_grilla = np.linspace(min(puntos['x']), max(puntos['x']), m)
    y_grilla = np.linspace(min(puntos['y']), max(puntos['y']), n)
    X, Y = np.meshgrid(x_grilla, y_grilla)
    linea_x = [x for x, y in coordenadas]
    linea_y = [y for x, y in coordenadas]

    # Graficar la grilla de puntos
    plt.scatter(X, Y, color='gray', s=2, label='Grilla')  # s es el tamaño de los puntos

    # Graficar los puntos
    plt.scatter(puntos['x'], puntos['y'], color='red', label='Puntos')

    # Graficar la línea
    plt.plot(linea_x, linea_y, color='blue', label='Línea')

    # Graficar puntos amarillos en los extremos de la línea
    plt.scatter(linea_x, linea_y, color='yellow',s=10, label='Puntos de Unión', zorder=5)

    # Añadir leyenda
    plt.legend()

  
    plt.text(0.5, -0.10, f"Error: {np.round(error)}      Grilla: [{m},{n}]", ha='center', va='center', transform=plt.gca().transAxes, fontsize=8)

    # Mostrar el gráfico
    plt.show()  