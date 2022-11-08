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

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_dst = cv2.equalizeHist(image_gray)
hist_dst = cv2.calcHist([image_dst], [0], None, bsize, ranges)
# 이미지 평활화 후 히스토그램 재계산

plt.figure(figsize=(12, 12))

titles = ['image', 'hist', 'image_str', 'hist_str', 'image_dst', 'hist_dst']
for idx, title in enumerate(titles):
    plt.subplot(3, 2, idx+1)
    plt.title(title)
    if idx % 2 == 0:
        plt.axis('off')
        plt.imshow(eval(title), cmap='gray')
    else:
        plt.bar(np.arange(64), eval(title).squeeze(1), color='k')
        # eval(title).squeeze(1) : 1차원으로 변환
        # hist.flatten()         : 1차원으로 변환

plt.show()