import numpy as np
class Result:

    def __init__(self):
        self.__globalResult:dict = {}
        self.__m = 0
        self.__n = 0
        self.__dataName = ""
        self.__algoName = ""
        self.__sol = []
        self.__bestError = 100000000
        self.__time = 2222222222

    def setMN(self,m_:int,n_:int):
        self.__m = m_
        self.__n = n_

    def setNames(self,dataName_:str,algoName_:str):
        self.__dataName = dataName_
        self.__algoName = algoName_

    def setSolutions(self,bestError_:float,puntos:list,time_:float)->bool:
        if len(puntos) != self.__m:
            return False
        if (bestError_ < 0):
            return False
        
        self.__sol = puntos
        self.__bestError = bestError_
        self.__time = time_

        return True
        
    def saveState(self):
        """
        Guarda Internamente en el globalResult el resultado de esta iteracion: name,m,n,puntos y best result
        """
        dataKey = self.__dataName[:-5] # Ej: titanium
        experimentKey: str = f"{self.__m}_{self.__n}" # Ej: 5_12

        if dataKey not in self.__globalResult:
            self.__globalResult[dataKey] = {}
        if self.__algoName not in self.__globalResult[dataKey]:
            self.__globalResult[dataKey][self.__algoName] = {}
        if experimentKey not in self.__globalResult[dataKey][self.__algoName]:
            self.__globalResult[dataKey][self.__algoName][experimentKey] = {"bestError": None, "solution": []}

        self.__globalResult[dataKey][self.__algoName][experimentKey]["bestError"] = self.__bestError
        self.__globalResult[dataKey][self.__algoName][experimentKey]["solution"] = self.__sol
        self.__globalResult[dataKey][self.__algoName][experimentKey]["timepo"] = self.__time

        

    

    def saveInFile(self,)->bool:
        """
        Guarda en un Archivo todo lo que paso 
        """
        print(self.__globalResult)

        pass

