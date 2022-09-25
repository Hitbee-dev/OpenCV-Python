import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
image[:] = 200
print(image.shape)

title1 = 'Changed'
cv2.namedWindow(title1, cv2.WINDOW_NORMAL)
cv2.resizeWindow(title1, 250, 100)
cv2.imshow(title1, image)
cv2.waitKey(0)
cv2.destroyAllWindows()