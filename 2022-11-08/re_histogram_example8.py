import numpy as np, cv2
import matplotlib.pyplot as plt
image1 = cv2.imread('D:/github/OpenCV-Python/2022-11-08/images/background.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('D:/github/OpenCV-Python/2022-11-08/images/test_image.jpg', cv2.IMREAD_GRAYSCALE)

# 이미지 사이즈 조정
image1 = image1[:image2.shape[0], :image2.shape[1]]

def onChange(x):
    alpha = cv2.getTrackbarPos('image1', 'image') / 100
    beta = cv2.getTrackbarPos('image2', 'image') / 100

    mul_img = cv2.addWeighted(image1, alpha, image2, beta, 0)

    hist = cv2.calcHist([mul_img], [0], None, [64], [0, 256])   # 히스토그램 계산

    plt.cla()
    plt.bar(np.arange(hist.shape[0]), hist.flatten(), color='b')
    plt.show(block=False)

    cv2.imshow('image', mul_img)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('image1', 'image', 0, 100, onChange)
cv2.createTrackbar('image2', 'image', 0, 100, onChange)

figure = plt.figure(figsize=(4,3))
plt.bar(np.arange(64), [0]*64, color='b')
plt.show()

cv2.waitKey()