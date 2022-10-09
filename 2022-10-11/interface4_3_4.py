import numpy as np
import cv2

image = np.zeros((400, 400), np.uint8)
image.fill(255)

eye = np.full((50, 100), 192, np.uint8)
image[100:150, 50:150] = eye
image[100:150, 200:300] = eye

nouse = np.full((70, 30), 192, np.uint8)
image[200:270, 150:180] = nouse

mouse = np.full((20, 70), 192, np.uint8)
image[300:320, 130:200] = mouse


cv2.imshow("robot face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()