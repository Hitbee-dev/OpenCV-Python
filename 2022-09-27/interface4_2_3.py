import numpy as np
import cv2

def onChange(value):
    global image, title
    image[:] = value
    cv2.imshow(title, image)

image = np.zeros((300, 500), np.uint8)
image[:] = 150
title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()