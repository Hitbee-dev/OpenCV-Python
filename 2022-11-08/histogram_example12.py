'''
연습문제12
영상처리에서 투영(projection)은 다음의 수식으로 표현된다.
OpenCV 함수 중에 cv2.reduce()함수를 이용해서 수식과 같이 수직 및 수평 방향 투영을 수행하는 프로그램을 작성하라.
cv2.reduce()는 차원을 감소시켜주며 최소값, 최대값, 평균값을 반환한다.

추가조건
1. 영상 파일을 읽어서 투영 히스토그램을 출력하시오.
2. OpenCV가 아닌 Matplotlib으로 히스토그램을 출력하시오.
'''

import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread('D:/github/OpenCV-Python/2022-11-08/images/hannam.jpg', cv2.IMREAD_GRAYSCALE)
image_v = cv2.reduce(image, dim=0, rtype=cv2.REDUCE_AVG) # dim=0 수직방향
image_h = cv2.reduce(image, dim=1, rtype=cv2.REDUCE_AVG) # dim=1 수평방향

def draw_histo(hist, shape, axis):
    if axis == 1: # 수직방향
        shape = (shape[1], shape[0])
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) # 정규화
    gap = hist_img.shape[1] / hist.shape[0]                 # 막대 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))                             # 막대 시작 좌표
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    if axis == 0:
        return cv2.flip(hist_img, 0)                            # 영상 좌우 반전
    elif axis == 1:
        return cv2.rotate(cv2.flip(hist_img, 0), cv2.ROTATE_90_CLOCKWISE)     # 영상 회전

hist_v = cv2.calcHist([image_v], [0], None, [64], [0, 256])   # 히스토그램 계산
hist_v_img = draw_histo(hist_v, image.shape, 0)               # 히스토그램 그리기

hist_h = cv2.calcHist([image_h], [0], None, [64], [0, 256])   # 히스토그램 계산
hist_h_img = draw_histo(hist_h, image.shape, 1)               # 히스토그램 그리기

plt.figure(figsize=(12, 8))

titles = ['image', 'hist_h_img', 'hist_v_img']
for idx, title in enumerate(titles):
    plt.subplot(2, 2, idx+1)
    plt.axis('off')
    plt.title(title)
    plt.imshow(eval(title), cmap='gray')

plt.show()