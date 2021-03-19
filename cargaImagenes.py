import cv2
import numpy as np
from conv import convolucion



IRGB= cv2.imread("001.jpg")
print(IRGB)
print(IRGB.shape)

IGS= cv2.cvtColor(IRGB, cv2.COLOR_BGR2GRAY)
cv2.imwrite("004GS.jpg",IGS)

print(IGS)

K=[[-1, 0, 1],[-1, 0 ,1],[-1, 0, 1]]
cv2.imwrite("004GS.jpg",convolucion(IGS,K))


fr = len(Ioriginal)
cr = len(Ioriginal[0])-(len(kernel[0])-1)
res = np.zeros((fr/2, cr/2), np.uint8)
for i in range(len(res)):
        for j in range(len(res[0])):
          res[i][j]=max(Ioriginal[i*2:(i+1)*2][j*2:(j+1)*2])
