# stretching

import numpy as np, cv2
import matplotlib.pyplot as plt

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) # 정규화
    print()
    gap = hist_img.shape[1] / hist.shape[0]                 # 막대 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))                             # 막대 시작 좌표
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)                            # 영상 좌우, 상하 반전 

def search_value_idx(hist, bias=0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)
        if hist[idx] > 0:
            return idx

image = cv2.imread("D:/github/OpenCV-Python/2022-11-08/images/dark_image.png", cv2.IMREAD_COLOR)

bsize, ranges = [64], [0, 256]

hist = cv2.calcHist([image], [0], None, bsize, ranges)   # 히스토그램 계산
hist_img = draw_histo(hist)                               # 히스토그램 그리기

## 화소값 할당
bin_width = ranges[1] / bsize[0]
low = search_value_idx(hist, 0) * bin_width
high = search_value_idx(hist, bsize[0] - 1) * bin_width

idx = np.arange(0, 256)
idx = (idx - low) / (high - low) * 255
idx[:int(low)] = 0
idx[int(high+1):] = 255

dst = cv2.LUT(image, idx.astype(np.uint8))
hist_dst = cv2.calcHist([dst], [0], None, bsize, ranges)   # 히스토그램 계산
hist_dst_img = draw_histo(hist_dst) 

titles = ["image", "hist_img", "dst", "hist_dst_img"]

plt.figure(figsize=(10, 10))

for idx, title in enumerate(titles):
    plt.subplot(2, 2, idx+1)
    plt.axis('off')
    plt.title(title)
    plt.imshow(eval(title), cmap='gray')

plt.show()