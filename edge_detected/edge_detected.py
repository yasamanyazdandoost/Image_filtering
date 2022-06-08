#YasamanYazdandoost 9708193
import cv2  #library OpenCV

path = 'yasi.jpg' #orginal image

image = cv2.imread(path, 1)

cv2.imshow('Original', image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

edgeDetected = cv2.Canny(image,100,200)
cv2.imwrite('yasi_edge_detected.jpg', edgeDetected)

cv2.imshow('Edge Detected' , edgeDetected)
cv2.waitKey(2000)
cv2.destroyAllWindows()