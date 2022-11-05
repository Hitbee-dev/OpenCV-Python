# normalize

import numpy as np, cv2

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

image = cv2.imread("D:/github/OpenCV-Python/2022-11-08/images/dark_image.png", cv2.IMREAD_COLOR)

hist = cv2.calcHist([image], [0], None, [32], [0, 256])   # 히스토그램 계산
hist_img = draw_histo(hist)                               # 히스토그램 그리기

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.waitKey(0)