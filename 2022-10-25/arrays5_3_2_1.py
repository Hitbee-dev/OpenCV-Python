import numpy as np, cv2

image = cv2.imread('D:/github/OpenCV-Python/2022-10-18/images/python_logo.png', cv2.IMREAD_COLOR)
# 이미지 불러오기

image = cv2.resize(image, dsize=(image.shape[1]//8, image.shape[0]//8), interpolation=cv2.INTER_LINEAR)
# 이미지 사이즈 조절(너무 크니까 8배 작게)
cv2.imshow('image',image)

image2 = np.where(image == 0, 255, image)
# 이미지 배경 색 흰색으로 변경
cv2.imshow('image2',image2)

image3 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# 이미지 흑백 전환
cv2.imshow('image3',image3)

image4 = np.where(image3 != 255, 0, image3)
# 배경을 제외한 나머지 색 전부 검은색으로 변환
cv2.imshow('image4', image4)
cv2.waitKey(0)