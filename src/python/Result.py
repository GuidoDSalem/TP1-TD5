import numpy as np
class Result:

    def __init__(self):
        self.__globalResult = {}
        self.__m = 0
        self.__n = 0
        self.__dataName = ""
        self.__algoName = ""
        self.__sol = []
        self.__bestError = 100000000

    def setMN(self,m_:int,n_:int):
        self.__m = m_
        self.__n = n_

    def setNames(self,dataName_:str,algoName_:str):
        self.__dataName = dataName_
        self.__algoName = algoName_

    def setSolutions(self,puntos:list[tuple[int,int]],bestError_:int)->bool:
        if(len(puntos != self.__m)):
            return False
        if (bestError_ < 0):
            return False
        
        self.__sol = puntos
        self.__bestError = bestError_

        return True
        
    def saveState(self):
        """
        Guarda Internamente en el globalResult el resultado de esta iteracion: name,m,n,puntos y best result
        """
        dataKey = self.__dataName[:-4] # Ej: titanium
        experimentKey = str(self.__m) + "_" + self.__n # Ej: 5_12
        self.__globalResult[dataKey][self.__algoName][experimentKey]["bestError"] = self.__bestError
        self.__globalResult[dataKey][self.__algoName][experimentKey]["solution"] = self.__sol

        

    

    def saveInFile(self,)->bool:
        """
        Guarda en un Archivo todo lo que paso 
        """
        print(self.__globalResult)

        pass

