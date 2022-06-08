#YasamanYazdandoost 9708193
import cv2  #library OpenCV

path = 'yasi_noisy_image.jpg'

noisy_image = cv2.imread(path, -1)

cv2.imshow('Noisy Image', noisy_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()

denoised = cv2.GaussianBlur(noisy_image, (3, 3), 2, borderType = cv2.BORDER_CONSTANT)
cv2.imwrite('yasi_denoised.jpg', denoised)

cv2.imshow('Denoised Image', denoised)
cv2.waitKey(2000)
cv2.destroyAllWindows()
