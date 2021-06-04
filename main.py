import cv2 as cv
import numpy as np

img = cv.imread('/home/user/Downloads/Santorini.jpg')
rows, cols, ch = img.shape

print("Height: ", rows)
print("Width: ", cols)

scaled_img = cv.resize(img, None, fx=1/2, fy=1/2)

matrix_t = np.float32([[1, 0, 100], [0, 1, 50]])
translated_img = cv.warpAffine(img, matrix_t, (cols, rows))

matrix_r = cv.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rotated_img = cv.warpAffine(img, matrix_r, (cols, rows))

cv.imshow("Original image", img)
cv.imshow("Scaled_img", scaled_img)
cv.imshow("Translated_img", translated_img)
cv.imshow("Rotated_img", rotated_img)
cv.waitKey(0)
cv.destroyAllWindows()
