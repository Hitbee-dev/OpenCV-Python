import numpy as np, cv2

image = cv2.imread('D:/github/OpenCV-Python/2022-10-18/images/python_logo.png', cv2.IMREAD_COLOR)
# 이미지 불러오기

image = cv2.resize(image, dsize=(image.shape[1]//8, image.shape[0]//8), interpolation=cv2.INTER_LINEAR)
# 이미지 사이즈 조절(너무 크니까 8배 작게)
cv2.imshow('image',image)

ret, thresh1 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
# 이미지 이진화
cv2.imshow('thresh1', thresh1)

image2 = 255 - thresh1
# 이미지 색 반전
cv2.imshow('image2', image2)
cv2.waitKey(0)