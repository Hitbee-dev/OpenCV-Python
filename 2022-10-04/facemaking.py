import numpy as np
import cv2

image = np.zeros((400, 400), np.uint8)
image.fill(255)                                 # 모든 원소에 255(흰색) 지정

eye = np.full((50, 100), 192, np.uint8)
image[100:150, 50:150] = eye
image[100:150, 200:300] = eye
image[200:220, 150:200] = eye[:20, :50]


cv2.imshow("robot face", image)

cv2.waitKey(0)
cv2.destroyAllWindows()