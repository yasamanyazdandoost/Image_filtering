#YasamanYazdandoost 9708193
import cv2  #library OpenCV

path = 'yasi.jpg' #orginal image

img = cv2.imread(path, 1) #flag=1 : colorful image
cv2.imshow('ColorFul Image', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

grayImage = cv2.imread(path, 0) #flag=0 : grayscale image
cv2.imshow('GrayScale Image', grayImage)
cv2.imwrite('yasi_grayscale.jpg', grayImage)
cv2.waitKey(2000)
cv2.destroyAllWindows()

(thresh, binaryImg) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary Image', binaryImg)
cv2.imwrite('yasi_binary.jpg', binaryImg)
cv2.waitKey(2000)
cv2.destroyAllWindows()