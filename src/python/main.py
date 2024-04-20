import json
import numpy as np
from algorithms.fuerzaBruta import fuerzaBruta
from algorithms.fuerzaBruta_v3 import fuerzaBrutaV3

from algorithms.backTracking import backTracking
from algorithms.pDinamica import pDinamica

import numpy as np
import matplotlib.pyplot as plt

# from algorithms.dinamicAlgoritm import dinamicAlgoritm
from Result import Result
import os

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
	ms = [5]
	ns = [5]
	k_breakpoints = [3,4,5]

	# # Por cada lista de Datos:
	result:Result = Result()
	# errors_listFB = []
	# errors_listBT = []
	# errors_listPD = []
	# breakpoints_list = [2,3,4,5]
 
	# for dataName in listaDeDatos:
	# 	path = dataPath + dataName

		# Cargamos los Datos
		# with open(path) as f:
		# 	instance = json.load(f)
			
		# 	for k in breakpoints_list:
		# 		bestError,solutions,time = fuerzaBrutaV3(6,6,k,instance)
		# 		errors_listFB.append(time)
		# 		bestError,solutions,time = backTracking(6,6,k, instance)
		# 		errors_listBT.append(time)
		# 		bestError,solutions,time = pDinamica(6, 6, k,instance)
		# 		errors_listPD.append(time)
    
	# errors_list = [errors_listFB, errors_listBT, errors_listPD]
	# plt.figure(figsize=(10, 6))
	# algorithm_names = ['FuerzaBruta', 'BackTracking', 'ProgDinamica']
	# breakpoints_lists = [breakpoints_list, breakpoints_list, breakpoints_list]
    # Plot errors vs breakpoints for each algorithm
	# for errors, breakpoints, algorithm_name in zip(errors_list, breakpoints_lists, algorithm_names):
	# 	plt.plot(breakpoints, errors, label=algorithm_name)

	# plt.xlabel('Breakpoints')
	# plt.ylabel('Time')
	# plt.title('Time vs Breakpoints')
	# plt.legend()
	# plt.grid(True)
	# plt.show()


	for dataName in listaDeDatos:
		path = dataPath + dataName

		# Cargamos los Datos
		with open(path) as f:
			instance = json.load(f)
			for k in k_breakpoints:
				for i in ms:
					for j in ns:

						result.setMN(i,j)


						# fuerza bruta 
						result.setNames(dataName,"FuerzaBruta")
						bestError,solutions,time = fuerzaBruta(i,j,k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

						#fuerza bruta 3
						# result.setNames(dataName,"FuerzaBruta3")
						# bestError,solutions,time = fuerzaBrutaV3(i,j,k,instance)
						# result.setSolutions(bestError,solutions,time)
						# result.saveState()
						
						#backtracking
						result.setNames(dataName,"BackTracking")
						bestError,solutions,time = backTracking(i, j,k, instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()


						# result.setNames(dataName,"DinamicAlgorithm")
						# bestError,solutions,time = dinamicAlgoritm(i, j, instance)
						# result.setSolutions(bestError,solutions,time)
						# result.saveState()

						#programacion dinamica
						result.setNames(dataName,"DinamicAlgorithm")
						bestError,solutions,time = pDinamica(i, j, k,instance,dataName)
						result.setSolutions(bestError,solutions,time)
						result.saveState()

	result.saveInFile()

if __name__ == "__main__":
	main()