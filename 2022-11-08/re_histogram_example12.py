'''
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
'''

import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-08/images/hannam.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

project1 = cv2.reduce(image, 0, cv2.REDUCE_AVG).ravel().astype(int)
project2 = cv2.reduce(image, 1, cv2.REDUCE_AVG).ravel().astype(int)

#print(image.shape)
#print(project1.shape, project2.shape)

_, ax = plt.subplots(2,2)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
ax[0,0].imshow(image, aspect="auto", cmap="gray")
ax[0,0].set_title("image")
ax[0,0].get_xaxis().set_ticks([])
ax[0,0].get_yaxis().set_ticks([])

ax[0,1].barh(np.arange(project1.shape[0]), project1)
ax[0,1].set_title("horizontal projection")

ax[1,0].bar(np.arange(project2.shape[0]), project2)
ax[1,0].invert_yaxis()
ax[1,0].set_title("vertical projection")

plt.show()