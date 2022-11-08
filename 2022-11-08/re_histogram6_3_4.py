import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-08/images/dark_image.png", cv2.IMREAD_COLOR)
# 영상 읽기

bsize, ranges = [64], [0,256]
# 계급 개수, 화소 범위

hist = cv2.calcHist([image], [0], None, bsize, ranges)
# 히스토그램 재계산

image_str = cv2.normalize(image, None, 0, 255., cv2.NORM_MINMAX)
hist_str = cv2.calcHist([image_str], [0], None, bsize, ranges)
# 이미지 정규화 후 히스토그램 재계산

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')

plt.subplot(2, 2, 2)
plt.bar(np.arange(64), hist.flatten(), color='k')

plt.subplot(2, 2, 3)
plt.imshow(image_str, cmap='gray')

plt.subplot(2, 2, 4)
plt.bar(np.arange(64), hist_str.flatten(), color='k')
plt.show()