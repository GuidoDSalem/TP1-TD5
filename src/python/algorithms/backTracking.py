
import numpy as np

def backTracking(Xs:int, Ys:int, datos):

    grid_x = np.linspace(min(datos["x"]), max(datos["x"]), num=Xs, endpoint=True)
    grid_y = np.linspace(min(datos["y"]), max(datos["y"]), num=Xs, endpoint=True)

    pass