'''
연습문제8
OpenCV 함수 중에서 cv2.addWeight()함수를 사용해서 두 영상을 합성하는 프로그램을 작성하시오.

추가조건
trackbar를 이용해서 각 영상의 반영 비율을 조절할 수 있도록
'''

import numpy as np, cv2

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) # 정규화
    gap = hist_img.shape[1] / hist.shape[0]                 # 막대 너비

    for i, h in enumerate(hist):
        x = int(round(i * gap))                             # 막대 시작 좌표
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)                            # 영상 좌우, 상하 반전 

image1 = cv2.imread('D:/github/OpenCV-Python/2022-11-08/images/background.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('D:/github/OpenCV-Python/2022-11-08/images/test_image.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 사이즈 조정
image1 = image1[:image2.shape[0], :image2.shape[1]]

def onChange(x):
    pass

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('image1', 'image', 0, 100, onChange)
cv2.createTrackbar('image2', 'image', 0, 100, onChange)

while True:
    alpha = cv2.getTrackbarPos('image1', 'image') / 100
    beta = cv2.getTrackbarPos('image2', 'image') / 100

    mul_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    cv2.imshow('image', mul_img)
    
    hist = cv2.calcHist([mul_img], [0], None, [64], [0, 256])   # 히스토그램 계산
    hist_img = draw_histo(hist)                               # 히스토그램 그리기
    cv2.imshow('hist_img', hist_img)
    cv2.waitKey(1)
