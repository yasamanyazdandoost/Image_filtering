
import cv2  #library OpenCV
import numpy as np

path = 'yasi.jpg' #orginal image

image = cv2.imread(path, 1)

def gaussian_filter(image):
    row, col, ch = image.shape
    gaussian = np.random.normal(0,100,(row,col,ch))
    gaussian = gaussian.reshape(row,col,ch)
    noisy_image = image + gaussian
    return noisy_image

noisy_image = gaussian_filter(image)
cv2.imwrite('yasi_noisy_image.jpg', noisy_image)

cv2.imshow('Original', image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()