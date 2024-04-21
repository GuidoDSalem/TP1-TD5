result.setNames(dataName,"FuerzaBruta2")
						bestError,solutions,time = fuerzaBrutaV3(i,j,k,instance)
						result.setSolutions(bestError,solutions,time)
						result.saveState()