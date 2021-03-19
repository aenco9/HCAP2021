import numpy as np

def convolucion(Ioriginal, kernel):
	'''Método encargado de realizar una convolución a una imagen
	Entrada:
	Ioriginal - imagen original en forma de matríz
	kernel -  kernel para barrer la imagen
	Salida:
	res - imagen resultante'''
	#fr - filas, cr - columnas
	fr = len(Ioriginal)-(len(kernel)-1)
	cr = len(Ioriginal[0])-(len(kernel[0])-1)
	res = np.zeros((fr, cr))

	#filas, matríz resultado
	for i in range(len(res)):
		#columnas, matríz resultado
		for j in range(len(res[0])):
			suma = 0
			#filas, kernel
			for m in range(len(kernel)):
				#columnas, kernel
				for n in range(len(kernel[0])):
					suma += kernel[m][n] * Ioriginal[m+i][n+j]
			res[i][j] = suma
	return res