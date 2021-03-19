import numpy as np

def convolucion(Imageno,Kernel):
    dim = len(Imageno)-(len(Kernel)-1)
    dim2= len(Imageno[0])-(len(Kernel[0])-1)
    Resultado= np.zeros(dim,dim2)
    
    for in in range(len(Resultado)):
        for j in range(len(Resultado[0])):
            suma=0
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+= Kernel[m][n]* Imageno[m+i][n+j]
            Resultado[i][j]=suma
    return Resultado

