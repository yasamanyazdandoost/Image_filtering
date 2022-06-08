import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('yasi.jpg', 0)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

prewitt_x = cv2.filter2D(img, -1, kernelx)
prewitt_y = cv2.filter2D(img, -1, kernely)
prewitt = prewitt_x + prewitt_y
cv2.imwrite('prewitt.jpg', prewitt)

cv2.imshow('Original', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Prewitt X', prewitt_x)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Prewitt Y', prewitt_x)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Prewitt', prewitt)
cv2.waitKey(2000)
cv2.destroyAllWindows()