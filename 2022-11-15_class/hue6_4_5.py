import numpy as np, cv2

img = cv2.imread('images/hue_image.jpg', cv2.IMREAD_COLOR)
HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue_img = np.copy(HSV_img)[:, :, 0] # Hue 채널만 가지고 오기

th = [50, 100]


def onThreshold(value):
    th[0] = cv2.getTrackbarPos("Hue_th1", "result")
    th[1] = cv2.getTrackbarPos("Hue_th2", "result")

    _, result = cv2.threshold(hue_img, th[1], 255, cv2.THRESH_TOZERO_INV)
    cv2.threshold(result, th[0], 255, cv2.THRESH_BINARY, result)
    cv2.imshow('result', result)


cv2.namedWindow("result")
cv2.createTrackbar("Hue_th1", "result", th[0], 255, onThreshold)
cv2.createTrackbar("Hue_th2", "result", th[1], 255, onThreshold)

cv2.imshow('img', img)
cv2.waitKey(0)