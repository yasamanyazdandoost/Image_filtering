#YasamanYazdandoost 9708193
import cv2  #library OpenCV

path = 'yasi.jpg' #orginal image

image = cv2.imread(path, 1)

cv2.imshow('Original', image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

blured = cv2.blur(image, (5, 5))
cv2.imwrite('yasi_blured.jpg', blured)

cv2.imshow('blured' , blured)
cv2.waitKey(2000)
cv2.destroyAllWindows()