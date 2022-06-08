import cv2
from matplotlib import pyplot as plt

image = cv2.imread('yasi.jpg', 0)
cv2.imshow('ys', image)
med = cv2.medianBlur(image, 5)
plt.figure(figsize=(11,6))
plt.subplot(121)
plt.imshow(image)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
cv2.imwrite('median_filter.jpg', med)
plt.imshow(med)
plt.title('Median Filter')
plt.xticks([])
plt.yticks([])
plt.show()