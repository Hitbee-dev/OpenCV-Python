import numpy as np, cv2

image1 = cv2.imread('D:/github/OpenCV-Python/2022-11-01/images/background.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('D:/github/OpenCV-Python/2022-11-01/images/test_image.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 사이즈 조정
image1 = image1[:image2.shape[0], :image2.shape[1]]

def onChange(x):
    pass

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('alpha', 'image', 0, 10, onChange)
cv2.createTrackbar('beta', 'image', 0, 10, onChange)

while True:
    alpha = cv2.getTrackbarPos('alpha', 'image') / 10
    beta = cv2.getTrackbarPos('beta', 'image') / 10

    mul_img = cv2.addWeighted(image1, alpha, image2, beta, 0)
    cv2.imshow('image', mul_img)
    cv2.waitKey(1)
