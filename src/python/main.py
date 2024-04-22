import json
import numpy as np
import os

from algorithms.fuerzaBruta import fuerzaBruta

from algorithms.backTracking import backTracking

from algorithms.pDinamica import pDinamica


from algorithms.Core import *

from Result import Result


BIG_NUMBER = 1e10 # Revisar si es necesario.

def main():

	# Path a los datos json
	dataPath = "data/"
	print(os.curdir)

	# Datos
	listaDeDatos = ["aspen_simulation.json","ethanol_water_vle.json","optimistic_instance.json","titanium.json","toy_instance.json"]
	listaDeDatos_sinjson = ["aspen_simulation","ethanol_water_vle","optimistic_instance","titanium","toy_instance"]
	
	
	# VALORES DE EXPERIMENTO
	ms = [5]
	ns = [5]
	breakpoints_list = [2,3,4,5]

	# Por cada lista de Datos:
	result:Result = Result()
 
	#--------------------------------para correr los algoritmos en si , graficos individuales-------------------------
	#todos estos graficos se guardan bajo las carpeta de graficos dentro de cada carpeta de dataset se guarda su grafico
	for dataName in listaDeDatos:
		path = dataPath + dataName

			#Cargamos los Datos
		with open(path) as f:
			instance = json.load(f)
			for k in breakpoints_list:
				for i in ms:
					for j in ns:
						print(f"DATA: {dataName},K: {k}, M: {i}, N: {j}")
						result.setMN(i,j)


							#fuerza bruta
						result.setNames(dataName,"FuerzaBruta")
						bestError,solutions,time = fuerzaBruta(i,j,k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

							#backtracking
						result.setNames(dataName,"BackTracking")
						bestError,solutionsX,solutionsY,time = backTracking(i, j,k, instance,dataName)
						result.setSolutions(bestError,solutionsX,time)
						result.saveState()
			
							#programacion dinamica
						result.setNames(dataName,"DinamicAlgorithm")
						bestError,solutionsX,solutionsY,time = pDinamica(i, j, k,instance,dataName)
						result.setSolutions(bestError,solutionsX,time)
						result.saveState()
       

	
	# #----------------para caclular diferencia de tiempos o errores  y gtaficarlos--------------------
	
	# #valor de breakpoint para comparar entre todos los datasets
	# valor_comparativo = 3	
 
	# tiempos_fuerza_bruta = []
	# tiempos_backtracking = []
	# tiempos_pdinamic = []

		
	# for dataName in listaDeDatos:
	# 	path = dataPath + dataName
	# 		# Cargamos los Datos
	# 	with open(path) as f:
	# 		instance = json.load(f)
	# 			#inicializamos las listas vacias asi no se superponen entre datasets
	# 		timeBT = [] 
				
	# 		timePD = []
	# 		errorPD = []
	
	# 		timeFB = []
				
	
	# 		for i in ms:
	# 			for j in ns:
	# 				for k in breakpoints_list:
	# 					#si el k es mas grande que la cantidad de xs para la grila no corre
	# 					if k>i:
	# 						raise ValueError("El k es mas grande que el x")
	
	# 					print(f"DATASET: {dataName} con {k} breakpoints\n")
							
	# 					#si queremos correr con fuerza bruta se hace demasiado lento igual y los tiempos de comparacion no lo valen tanto
	# 					#esta condicion la ponemos porque sino se hace muy largo el tiempo de ejecucion
	# 					if k < 5:
	# 						print("corriendo fuerza bruta....")
	# 						bestError,solutions,time0 = fuerzaBruta(6, 6,k, instance, dataName)
	# 						timeFB.append(time0)
								
	# 					print("corriendo back tracking....")
	# 					bestError,solutionsX,solutionsY,time1 = backTracking(i,j,k, instance, dataName)
	# 					timeBT.append(time1)
							
	# 					print("corriendo programacion dinamica....")
	# 					bestError2,solutionsX,solutionsY,time2 = pDinamica(i,j, k,instance,dataName)
	# 					timePD.append(time2)
	# 					errorPD.append(bestError2)
		
	# 					if k == valor_comparativo:
	# 						if k > 5: 
	# 							bestError,solutions,time0 = fuerzaBruta(i, j,k, instance, dataName)
         
	# 						tiempos_fuerza_bruta.append(time0)
	# 						tiempos_backtracking.append(time1)
	# 						tiempos_pdinamic.append(time2)


	# 				####### grafico los tiempos  y errores
	# 				### comparo bt y pd si quiero comparar los 3 comento esto y descomento lo otro
	# 				#si comparo solo bt y pd
	# 				time_list = [timeBT, timePD]
	# 				algorithm_names = ['Back Tracking', 'ProgDinamica']
	# 				breakpoints_lists  = [breakpoints_list, breakpoints_list]
		
	# 				#ver la diferencia de tiempo por promedio de BT con PD 
	# 				sum_t = 0
	# 				for i in range(0,len(timeBT)-1):
	# 					dif_tiempo = abs(timeBT[i] - timePD[i])
	# 					sum_t += dif_tiempo
	# 				avg_t = (sum_t/len(timeBT))
		

	# 				# ### si compar con fuerza bruta (corre mil veces mas lento ), descomentar esto  y comentar lo otro
	# 				# #si comparo fb, bt y pd
	# 				# time_list = [timeFB, timeBT, timePD]
	# 				# algorithm_names = ['Fuerza Bruta','Back Tracking', 'ProgDinamica']
	# 				# breakpoints_lists  = [breakpoints_list, breakpoints_list, breakpoints_list]
       
	# 				# #ver la diferencia de tiempo por promedio de FB con BT
	# 				# sum_t = 0
	# 				# for i in range(0,len(timeFB)-1):
	# 				# 	dif_tiempo = abs(timeFB[i] - timeBT[i])
	# 				# 	sum_t += dif_tiempo
	# 				# avg_t = (sum_t/len(timeFB))
       
       
	# 				#### estos graficos se encuentran bajo la carpeta de graficos comparaciones
     
     
	# 				#grafico de comparacion de tiempos vs breakpoints
	# 				comparacion_tiempo(time_list, algorithm_names, breakpoints_lists, round(avg_t,2), instance, dataName, i, j)
						
	# 				#grafico los errores con breakpoints
	# 				comparacion_errores(errorPD, breakpoints_list, instance, dataName, i, j)
		
	# 	#comparacion de tiempos segun los diferentes data sets dados con un k fijo
	# 	comparacion_tiempos_dataset(tiempos_fuerza_bruta, tiempos_backtracking, tiempos_pdinamic, listaDeDatos_sinjson )
  
	
						

if __name__ == "__main__":
	main()