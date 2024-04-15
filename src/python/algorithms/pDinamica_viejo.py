

# import numpy as np
# import time
# from algorithms.Core import *

# def pDinamica(m:int,n:int,k:int, datos):
   
#     start = time.time()
	
#     #creamos la grilla en x y en y para los datos 
#     gridX:list = np.linspace(min(datos["x"]), max(datos["x"]), num=m, endpoint=True)
#     gridY:list = np.linspace(min(datos["y"]), max(datos["y"]), num=n, endpoint=True)
    
#     #sacamos el primer y ultimo elemento de la grilla x para trabajr unicamente con las columnas del medio
#     conjunto_medio:list = gridX[1:-1]

#     # creamos una lista que va a contener todas las combinaciones posibles de como separar las columnas del medio dado k-2
#     listas_medio = []
#     listasCombinatorias(conjunto_medio,[],listas_medio,k-2)

#     #agregamos el primer y ultimo elemento a cada lista 
#     listas_medio = [[gridX[0]] + lista + [gridX[-1]] for lista in listas_medio]

#     bestRes = []
#     bestSubGridX =  [] 
#     bestError = 100000000000001

#     # Creo variables globales
#     global DiccionarioDeErrores
#     DiccionarioDeErrores = dict()

#     for i in range(k):
#         bestRes.append(gridY[-1])

   
#     #con cada subgrilla probamos fuerza bruta recursiva que recursivamente recorre todas las posibles combinaciones y devuelve el mejor error de esa subgrillaa
#     for subGridX in listas_medio:
#         print(subGridX)
#         res = []
       
#         #esto lo hice porque la lista estba vacia para darles valores inciales porque 
#         #sino en la priemra iteracion no podia iterar sobre valoers vacios por eso daba el lsit index out of range [1]
#         for i in range(len(subGridX)):
#             res.append(gridY[0])
        
#         errorActual = 100000000000001
        
#         errorActual = pDinamicaRecursiva(subGridX,gridY,errorActual, datos)
        
#         #si otra subgrilla tiene un mejor error guarda esa 
#         if(errorActual < bestError):
#             bestSubGridX = subGridX.copy()
#             bestError = errorActual
#             bestRes = res.copy()    
    
#     end = time.time()

#     totalTime = (end - start) * 1000


#     plot_puntos_y_linea(datos,bestSubGridX,bestRes,m,n,"ProgramacionDinamica",bestError,totalTime)

#     print(f"\nGridY: {gridY}")
#     print(f"\n\nTIEMPO: {totalTime}, FUNCION:{bestRes}\n")
    

#     return np.round(bestError,decimals=2),bestRes,np.round(totalTime,decimals=2)

 

# def pDinamicaRecursiva(gridX,gridY,xs:list,ys:list,res:list,bestError,datos):

#     # caso base: estoy parada en el ultimo segmento
#     if(len(gridX) == len(xs)):
#         clave = ((listaX[0],listaY[0]),(listaX[1],listaY[1]))
#         if (clave in DiccionarioDeErrores):
#             error_actual = DiccionarioDeErrores[clave]
#         else:
#             error_actual = errorAB(listaX[0], listaY[0], listaX[1], listaY[1], datos)
#             nueva_clave = clave
#             DiccionarioDeErrores[nueva_clave] = error_actual # defino nueva clave en mi diccionario, una que no habia calculado antes
#         return error_actual

#     else: # caso recursivo
#         error_actual = errorAB(listaX[0], listaY[0], listaX[1], listaY[1], datos)
#         errorTotal = error_actual + pDinamicaRecursiva(listaX[1:], listaY[1:], datos)  # Llamar recursivamente a la función con la lista de puntos restante
#         return errorTotal



    
#     #poda de optamalidad: si la rama que se esta calculando es mas grande que el mejor reusltado hasta ahora, descartala 
#     if(errorBreakPoints(xs,ys,datos) > errorBreakPoints(gridX,res,datos)):
#         return errorBreakPoints(xs,ys,datos)
    
#     #Caso Base
#     if(len(gridX) == len(xs)):
#         error_actual = 0
#         puntos = []
#         for i in range(len(xs) - 1):
#                 puntos.append((xs[i],ys[i]))
#                 puntos.append((xs[i+1],ys[i+1]))
#                 clave = (puntos[0],puntos[1])
#                 if (clave in DiccionarioDeErrores): # Si ya tengo el error entre estos dos puntos almacenado en mi diccionario, es decir ya lo calculé antes...
#                     error_actual = DiccionarioDeErrores[clave]
#                 else:
#                     error_actual = errorAB(xs[i],ys[i],xs[i+1],ys[i+1],datos)
#                     nueva_clave = clave
#                     DiccionarioDeErrores[nueva_clave] = error_actual # defino nueva clave en mi diccionario, una que no habia calculado antes
#                 errorBP += error_actual
#                 puntos.clear()
        
#         errorActual = errorBreakPoints(xs,res,datos) 
#         if(errorBP < errorActual):
#             # bestError = errorBP
#             res.clear()
#             res.extend(ys)
#             errorActual = errorBP
#             print(f"RES: {res},ERROR: {errorBP}")
#             bestError = errorBP
#         return bestError 
    
#     #Caso recursivo
#     i = len(xs)
#     xs.append(gridX[i])
#     currentBestError = bestError
#     for j in gridY:
#         ys.append(j)
#         error = pDinamicaRecursiva(gridX,gridY,xs,ys,res,currentBestError,datos)
#         if(error < currentBestError):
#             currentBestError = error
#         ys.pop()
#     xs.pop()

#     return currentBestError
    
# '''

















#     '''
#     # caso base: estoy parada en el ultimo segmento
#     if(len(gridX) == len(xs)):
#         #return error minimo
    
#     # caso recursivo
#     #else:
#     # Calcular error en donde estoy parada
#     error_actual = errorAB(listaX[0], listaY[0], listaX[1], listaY[1], datos)

    
#     # Llamar recursivamente a la función con la lista de puntos restante
#     errorTotal = error_actual + pDinamicaRecursiva(listaX[1:], listaY[1:], datos)
    
#     #return errorTotal
    

#     errorTotal = 0
#     error_actual = 0
#     puntos = []
#     for i in range(len(gx) - 1):
#         for j in range(len(gy) - 1):
#             puntos.append((gx[i],gy[j]))
#             puntos.append((gx[i+1],gy[j]))
#             clave = (puntos[0],puntos[1])
#             if (clave in DiccionarioDeErrores): # Si ya tengo el error entre estos dos puntos almacenado en mi diccionario, es decir ya lo calculé antes...
#                 error_actual = DiccionarioDeErrores[clave]
#             else:
#                 error_actual = errorAB(gx[i],gy[j],gx[i+1],gy[j+1],datos)
#                 nueva_clave = clave
#                 DiccionarioDeErrores[nueva_clave] = error_actual # defino nueva clave en mi diccionario, una que no habia calculado antes
#             errorTotal += error_actual
#             puntos.clear()
    
#     return errorTotal
# '''
# '''
# def errorBreakPoints_recursivo(listaX, listaY, datos):
#     # Caso base: Si solo hay un punto en la lista, retornar 0 como error total
#     if len(listaX) <= 1:
#         return 0
    
#     # Calcular error entre el primer punto y el segundo punto
#     error_actual = errorAB(listaX[0], listaY[0], listaX[1], listaY[1], datos)
    
#     # Llamar recursivamente a la función con la lista de puntos restante
#     errorTotal = error_actual + errorBreakPoints_recursivo(listaX[1:], listaY[1:], datos)
    
#     return errorTotal

# def errorBreakPoints_recursivo(listaX, listaY, datos, DiccionarioDeErrores):
    
#     if len(listaX) <= 1:
#         return 0
    
#     # Calcular clave para el diccionario
#     clave = ((listaX[0], listaY[0]), (listaX[1], listaY[1]))
    
#     # Si la clave ya está en el diccionario, obtener el error almacenado
#     if clave in DiccionarioDeErrores:
#         error_actual = DiccionarioDeErrores[clave]
#     else:
#         # Calcular error entre el primer punto y el segundo punto
#         error_actual = errorAB(listaX[0], listaY[0], listaX[1], listaY[1], datos)
#         # Guardar el error en el diccionario
#         DiccionarioDeErrores[clave] = error_actual
    
#     # Llamar recursivamente a la función con la lista de puntos restante
#     errorTotal = error_actual + errorBreakPoints_recursivo(listaX[1:], listaY[1:], datos, DiccionarioDeErrores)
    
#     return errorTotal

# '''










# '''
#     #poda de optamalidad: si la rama que se esta calculando es mas grande que el mejor reusltado hasta ahora, descartala 
#     if(errorBreakPoints(xs,ys,datos) > errorBreakPoints(gridX,res,datos)):
#         return errorBreakPoints(xs,ys,datos)
    
#     #Caso Base
#     if(len(gridX) == len(xs)):
        
#         errorBP = errorBreakPoints_dinamico(xs,ys,datos)
        
#         if (error_xs_res == -1):
#             errorActual = errorBreakPoints_dinamico(xs,res,datos) # Primera ejecución del caso base
#             error_xs_res = errorActual
        
#         else:
#             errorActual = error_xs_res 

#         # print(f"XY: {ys}, Error: {np.round(errorBP,decimals=2)}")
#         if(errorBP < errorActual):
#             # bestError = errorBP
#             res.clear()
#             res.extend(ys)
#             errorActual = errorBP
#             error_xs_res = errorBreakPoints_dinamico(xs,res,datos) 
#             print(f"RES: {res},ERROR: {errorBP}")
#             bestError = errorBP

#         return bestError 
    
#     #Caso recursivo
#     i = len(xs)
#     xs.append(gridX[i])
#     currentBestError = bestError
#     for j in gridY:
#         ys.append(j)
#         error = pDinamicaRecursiva(gridX,gridY,xs,ys,res,currentBestError,datos)
#         if(error < currentBestError):
#             currentBestError = error
#         ys.pop()
#     xs.pop()

#     return currentBestError
#     '''