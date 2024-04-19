import json
import numpy as np
from algorithms.fuerzaBruta import fuerzaBruta
from algorithms.backTracking import backTracking

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
	#listaDeDatos = ["optimistic_instance.json"]

	# VALORES DE EXPERIMENTO
	ms = [3] #cantidad de columnas
	ns = [6] #cantidad de filas
	k_breakpoints = 3

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

			for i in ms:
				for j in ns:

					result.setMN(i,j)


					# fuerza bruta 
					result.setNames(dataName,"FuerzaBruta")
					bestError,solutions,time = fuerzaBruta(i,j,k_breakpoints,instance)
					result.setSolutions(bestError,solutions,time)
					result.saveState()

	 			    #fuerza bruta 3
					result.setNames(dataName,"FuerzaBruta3")
					bestError,solutions,time = fuerzaBrutaV3(i,j,k_breakpoints,instance)
					result.setSolutions(bestError,solutions,time)
					result.saveState()
					
					#backtracking
					# result.setNames(dataName,"BackTracking")
					# bestError,solutions,time = backTracking(i, j,k_breakpoints, instance)
					# result.setSolutions(bestError,solutions,time)
					# result.saveState()
					
					#backtracking
					result.setNames(dataName,"BackTracking")
					bestError,solutions,time = backTracking(i, j,k_breakpoints, instance)
					result.setSolutions(bestError,solutions,time)
					result.saveState()

					#programacion dinamica
					# result.setNames(dataName,"ProgramacionDinamica")
					# bestError,solutions,time = pDinamica(i, j, instance)
					# result.setSolutions(bestError,solutions,time)
					# result.saveState()

					#programacion dinamica
					result.setNames(dataName,"DinamicAlgorithm")
					bestError,solutions,time = pDinamica(i, j, k_breakpoints,instance)
					result.setSolutions(bestError,solutions,time)
					result.saveState()

	result.saveInFile()








"""

############################  Original  ##########################
	# Ejemplo para leer una instancia con json
	instance_name = "titanium.json"
	# filename = "../../data/" + instance_name
	filename = "data/" + instance_name
	print(os.getcwd())

	
	with open(filename) as f:
		instance = json.load(f)
	
	K = instance["n"]
	# Discreciones en X
	m = 6
	# Discreciones en Y
	n = 6

	N = 5
	
	# Ejemplo para definir una grilla de m x n.
	grid_x = np.linspace(min(instance["x"]), max(instance["x"], num=m, endpoint=True)
	grid_y = np.linspace(min(instance["y"]), max(instance["y"]), num=n, endpoint=True)


	# TODO: aca se deberia ejecutar el algoritmo.

	best = {}
	best['sol'] = [None]*(N+1)
	best['obj'] = BIG_NUMBER
	
	# Posible ejemplo (para la instancia titanium) de formato de solucion, y como exportarlo a JSON.
	# La solucion es una lista de tuplas (i,j), donde:
	# - i indica el indice del punto de la discretizacion de la abscisa
	# - j indica el indice del punto de la discretizacion de la ordenada.
	best['sol'] = [(0, 0), (1, 0), (2, 0), (3, 2), (4, 0), (5, 0)]
	best['obj'] = 5.927733333333335

	# Represetnamos la solucion con un diccionario que indica:
	# - n: cantidad de breakpoints
	# - x: lista con las coordenadas de la abscisa para cada breakpoint
	# - y: lista con las coordenadas de la ordenada para cada breakpoint
	solution = {}
	solution['n'] = len(best['sol'])
	solution['x'] = [grid_x[x[0]] for x in best['sol']]
	solution['y'] = [grid_y[x[1]] for x in best['sol']]
	solution['obj'] = best['obj']

	# Se guarda el archivo en formato JSON
	with open('solution_' + instance_name, 'w') as f:
		json.dump(solution, f)
"""
	
if __name__ == "__main__":
	main()