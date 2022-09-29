import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8)
print(image)

title1 = 'Position1'
cv2.namedWindow(title1)
cv2.imshow(title1, image)
cv2.waitKey(0)
cv2.destroyAllWindows()