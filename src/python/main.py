import json
import numpy as np
import os

from algorithms.fuerzaBruta import fuerzaBruta
from algorithms.fuerzaBrutaV2 import fuerzaBrutaV2

from algorithms.backTracking_v3 import backTrackingV3
from algorithms.backTracking import backTracking

from algorithms.pDinamica import pDinamica
from algorithms.pDinamica_v3 import pDinamicaV3

from algorithms.Core import *

from Result import Result


BIG_NUMBER = 1e10 # Revisar si es necesario.

def main():

	# Json: "n" = cantidad de puntos, "x" = Lista de Cordenadas x, "y" = Lista de Coordenadas y

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
	k_breakpoints = [3,4,5]

	# # Por cada lista de Datos:
	result:Result = Result()
	
    #--------------------------------para caclular diferencia de tiempos o errores -------------------------------------
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
				#if k < 5:
				#	bestError,solutions,time0 = fuerzaBruta(6, 6,k, instance)
				#	timeFB.append(time0)
				#	errorFB.append(bestError)
				#else:
				#	timeFB.append(timeFB[-1])
				#	errorFB.append(errorFB[-1])
				bestError,solutions,time1 = pDinamica(6, 6,k, instance, dataName)
				timeBT.append(time1)
				errorBT.append(bestError)
				bestError,solutionsX,solutionsY,time2 = pDinamicaV3(6,6, k,instance,dataName)
				timePD.append(time2)
				errorPD.append(time2)
    
    
			#ver la diferencia de tiempo por promedio multiplicado 
			sum_t = 0
			for i in range(0,len(timeBT)-1):
				dif_tiempo = abs(timeBT[i] - timePD[i])
				sum_t += dif_tiempo
			avg_t = (sum_t/len(timeBT))
   
   
			print(avg_t)
			
			#si comparo solo bt y pd
			time_list = [timeBT, timePD]
			errors_list = [errorBT, errorPD]
			algorithm_names = ['progdinamica', 'ProgDinamica3']
			breakpoints_lists  = [breakpoints_list, breakpoints_list]
   
			#si comparo solo fb, bt y pd
			#time_list = [timeFB, timeBT, timePD]
			#errors_list = [errorFB, errorBT, errorPD]
			#algorithm_names = ['Fuerzaruta','BackTracking', 'ProgDinamica']
			#breakpoints_lists  = [breakpoints_list, breakpoints_list, breakpoints_list]
			
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

						result.setMN(i,j)


						# fuerza bruta: f-`ython` -guido
						result.setNames(dataName,"FuerzaBruta")
						bestError,solutions,time = fuerzaBruta(i,j,k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

						#fuerza bruta 2 : esta es f-cpp
						result.setNames(dataName,"FuerzaBruta2")
						bestError,solutions,time = fuerzaBrutaV2(i,j,k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()
							
						#backtracking_ f-python-guido
						result.setNames(dataName,"BackTracking")
						bestError,solutionsX,solutionsY,time = backTracking(i, j,k, instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()
		
						
						# backtrackingV3: f-cpp
						result.setNames(dataName,"BackTrackingV3")
						bestError,solutions,time = backTrackingV3(i, j,k, instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

						#programacion dinamica: del branch f-cpp
						result.setNames(dataName,"DinamicAlgorithm")
						bestError,solutions,time = pDinamica(i, j, k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()
		
						#programacion dinamica V3: del branch f-python guido
						result.setNames(dataName,"DinamicAlgorithmv3")
						bestError,solutionsX,solutionsY,time = pDinamicaV3(i, j, k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

						
		


	result.saveInFile()

	 			    
		

if __name__ == "__main__":
	main()