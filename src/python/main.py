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
	# listaDeDatos = ["titanium.json"]
	# gmarraffini@fi.uba.ar
	# VALORES DE EXPERIMENTO
	ms = [6]
	ns = [6]
	k_breakpoints = [3]

	# # Por cada lista de Datos:
	result:Result = Result()
	
    #----------------para caclular diferencia de tiempos o errores --------------------
	breakpoints_list = [2,3,4,5,6]
	
	for dataName in listaDeDatos:
		path = dataPath + dataName

		# Cargamos los Datos
		with open(path) as f:
			instance = json.load(f)

			timeBT = [] 
			errorBT = []
			timePD = []
			errorPD = []
			timeFB = []
			errorFB = []
        
			for k in breakpoints_list:
				print(f"------------DATASET-----------: {dataName} con {k} breakpoints\n")
				# if k < 5:
				# 	bestError,solutions,time0 = fuerzaBruta(6, 6,k, instance, dataName)
				# 	timeFB.append(time0)
				# 	errorFB.append(bestError)
				# else:
				# 	timeFB.append(timeFB[-1])
				# 	errorFB.append(errorFB[-1])
				bestError,solutionsX,solutionsY,time1 = backTracking(6, 6,k, instance, dataName)
				timeBT.append(time1)
				errorBT.append(bestError)
				bestError2,solutionsX,solutionsY,time2 = pDinamica(6,6, k,instance,dataName)
				timePD.append(time2)
				errorPD.append(bestError2)
    
    
			#ver la diferencia de tiempo por promedio multiplicado 
			sum_t = 0
			for i in range(0,len(timeBT)-1):
				dif_tiempo = abs(timeBT[i] - timePD[i])
				sum_t += dif_tiempo
			avg_t = (sum_t/len(timeBT))
   
			
			#si comparo solo bt y pd
			time_list = [timeBT, timePD]
			errors_list = [errorBT, errorPD]
			algorithm_names = ['Back Tracking', 'ProgDinamica']
			breakpoints_lists  = [breakpoints_list, breakpoints_list]
   
			#si comparo solo fb, bt y pd
			# time_list = [timeFB, timeBT, timePD]
			# errors_list = [errorFB, errorBT, errorPD]
			# algorithm_names = ['Fuerza Bruta','back tracking', 'ProgDinamica']
			# breakpoints_lists  = [breakpoints_list, breakpoints_list, breakpoints_list]
			
			comparacion_tiempo(time_list, algorithm_names, breakpoints_lists, round(avg_t,2), instance, dataName, 6, 6)
			comparacion_errores(errors_list, algorithm_names, breakpoints_lists, round(avg_t,2), instance, dataName, 6, 6)
  

	#--------------------------------para correr los algoritmos en si , graficos individuales-------------------------
	for dataName in listaDeDatos:
		path = dataPath + dataName

		# Cargamos los Datos
		with open(path) as f:
			instance = json.load(f)
			for k in k_breakpoints:
				for i in ms:
					for j in ns:

						print(f"DATA: {dataName},K: {k}, M: {i}, N: {j}")

						result.setMN(i,j)


						# fuerza bruta
						result.setNames(dataName,"FuerzaBruta")
						bestError,solutions,time = fuerzaBruta(i,j,k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

						# #backtracking
						result.setNames(dataName,"BackTracking")
						bestError,solutionsX,solutionsY,time = backTracking(i, j,k, instance,dataName)
						result.setSolutions(bestError,solutionsX,time)
						result.saveState()
		
						#programacion dinamica
						result.setNames(dataName,"DinamicAlgorithm")
						bestError,solutionsX,solutionsY,time = pDinamica(i, j, k,instance,dataName)
						result.setSolutions(bestError,solutionsX,time)
						result.saveState()
						print(f"TIEMPO PD V1: {time}") 
						
						



if __name__ == "__main__":
	main()