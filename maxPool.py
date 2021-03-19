import cv2
import numpy as np

def maxPooling(Ioriginal):
    filas = len(Ioriginal)//2
    columnas = len(Ioriginal[0])//2

    matrizresultado = np.zeros((filas, columnas), np.uint8) #matríz resultado

    for i in range(0,filas):
        for j in range(0,columnas):
            a=Ioriginal[i*2:i*2+2, j*2:j*2+2]
            a=a.flatten()
            print(a)
            matrizresultado[i][j] = max(a)
    return matrizresultado

