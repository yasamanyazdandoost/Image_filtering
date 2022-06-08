#YasamanYazdandoost 9708193
import cv2  #library OpenCV

path = 'yasi.jpg' #orginal image

Image = cv2.imread(path, 1)

cv2.imshow('Original', Image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

alpha = 1.5 # Contrast (1.0-3.0)
beta = 0 # Brightness (0-100)

high_contrast = cv2.convertScaleAbs(Image, alpha=alpha, beta=beta)
cv2.imwrite('yasi_high_contrast.jpg', high_contrast)

cv2.imshow('High Contrast', high_contrast)
cv2.waitKey(2000)
cv2.destroyAllWindows()

alpha = 0.5

low_contrast = cv2.convertScaleAbs(Image, alpha=alpha, beta=beta)
cv2.imwrite('yasi_low_contrast.jpg', low_contrast)

cv2.imshow('Low Contrast', low_contrast)
cv2.waitKey(2000)
cv2.destroyAllWindows()