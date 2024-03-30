import json
import numpy as np
import os

from algorithms.fuerzaBruta import fuerzaBruta
from algorithms.backTracking import backTracking

from algorithms.dinamicAlgoritm import dinamicAlgoritm
from Result import Result

BIG_NUMBER = 1e10 # Revisar si es necesario.

def main():

	# Json: "n" = cantidad de puntos, "x" = Lista de Cordenadas x, "y" = Lista de Coordenadas y

	# Path a los datos json
	dataPath = "data/"
	# Datos
	#listaDeDatos = ["aspen_simulation.json","ethanol_water_vle.json","optimistic_instance.json","titanium.json","toy_instance.json"]
	listaDeDatos = ["toy_instance.json"]
 
	# VALORES DE EXPERIMENTO
	ms = [2]
	ns = [2]

	


	# Por cada lista de Datos:
	result:Result = Result()
	
	for dataName in listaDeDatos:
		path = dataPath + dataName

		# Cargamos los Datos
		with open(path) as f:
			instance = json.load(f)

			for i in ms:
				for j in ns:

					result.setMN(i,j)

					result.setNames(dataName,"FuerzaBurta")
					bestError,solutions,time = fuerzaBruta(i, j, instance)
					result.setSolutions(bestError,solutions,time)
					result.saveState()

					# result.setNames(dataName,"BackTracking")
					# bestError,solutions = backTracking(i, j, instance)
					# result.setSolutions(bestError,solutions)
					# result.saveState()


					# result.setNames(dataName,"DinamicAlgorithm")
					# bestError,solutions = backTracking(i, j, instance)
					# result.setSolutions(bestError,solutions)
					# result.saveState()

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
	grid_x = np.linspace(min(instance["x"]), max(instance["x"]), num=m, endpoint=True)
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