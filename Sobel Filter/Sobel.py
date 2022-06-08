import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('yasi.jpg', 0)

sobel_x = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
sobel_y = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)
sobel = sobel_x + sobel_y

cv2.imwrite('sobel.jpg', sobel)

cv2.imshow('Original', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Sobel X', sobel_x)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Sobel Y', sobel_y)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Sobel', sobel)
cv2.waitKey(2000)
cv2.destroyAllWindows()