import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-29/images/car_image.jpg", cv2.IMREAD_GRAYSCALE)

mask = np.array([[0, 1, 0],
                [1, 1, 1],
                [0, 1, 0]], np.uint8)

ret, thresh1 = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

open_img = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, mask)
close_img = cv2.morphologyEx(thresh1, cv2.MORPH_CLOSE, mask, iterations=1)

plt.figure(figsize = (12, 5))

plt.subplot(1, 3, 1)
plt.title("image")
plt.imshow(image, cmap="gray")

plt.subplot(1, 3, 2)
plt.title("open_img")
plt.imshow(open_img, cmap="gray")

plt.subplot(1, 3, 3)
plt.title("close_img")
plt.imshow(close_img, cmap="gray")

plt.show()
