import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
title1 = "Keyboard Event"
cv2.namedWindow(title1)
cv2.imshow(title1, image)

result = ""
while True:
    key = cv2.waitKeyEx(100)
    if key == 2293760:
        break
    elif key == 3014656:
        result = ""
    try:
        result += chr(key)
        print(result)
    except ValueError:
        pass
cv2.destroyAllWindows()