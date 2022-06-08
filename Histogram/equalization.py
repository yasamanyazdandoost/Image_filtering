import cv2
from matplotlib import pyplot as plt

img = cv2.imread('yasi.jpg', 0)

equ = cv2.equalizeHist(img)
cv2.imwrite('equ.jpg', equ)

cv2.imshow('Original', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.imshow('Histogram Equalization', equ)
cv2.waitKey(2000)
cv2.destroyAllWindows()
plt.hist(equ.ravel(), 256, [0, 256])
plt.show()
