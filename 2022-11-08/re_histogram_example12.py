import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-08/images/hannam.jpg", cv2.IMREAD_COLOR)
# 영상 읽기

image_str = cv2.normalize(image, None, 0, 255., cv2.NORM_MINMAX)

image_v = cv2.reduce(image_str, dim=0, rtype=cv2.REDUCE_AVG) # dim=0 수직방향
image_h = cv2.reduce(image_str, dim=1, rtype=cv2.REDUCE_AVG) # dim=1 수평방향

bsize, ranges = [64], [0,256]
# 계급 개수, 화소 범위

hist_v = cv2.calcHist([image_v], [0], None, bsize, ranges)
hist_h = cv2.calcHist([image_h], [0], None, bsize, ranges)
# 히스토그램 재계산


plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')

plt.subplot(2, 2, 2)
plt.bar(np.arange(64), hist_v.flatten(), color='k')

plt.subplot(2, 2, 3)
plt.bar(np.arange(64), hist_h.flatten(), color='k')

plt.show()