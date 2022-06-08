import cv2
import numpy as np

path = 'yasi.jpg'
img = cv2.imread(path, 0) #grayscale
cv2.imshow('Original Image', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

im1 = cv2.blur(img, (5, 5))
im2 = cv2.boxFilter(img, -1, (10, 10), normalize=True)

ave = np.hstack((im1, im2))
cv2.imwrite('averaging_filter.jpg', ave)
cv2.imshow('averaging filter', ave)
cv2.waitKey(2000)
cv2.destroyAllWindows()
cv2.waitKey(1)