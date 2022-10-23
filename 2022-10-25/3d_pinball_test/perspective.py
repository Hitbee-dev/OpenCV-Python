import numpy as np
import cv2

# 이미지 받아오는 부분
image_path = 'D:/github/OpenCV-Python/2022-10-25/3d_image.png'
img = cv2.imread(image_path)

# 이미지 그레이스케일 해서 정확하게 확인
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지 외곽선 추출
contours, hierarchy = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

c_data = []
for contour in contours:
    c_data = contour.reshape(-1, 2)
    # img2 = cv2.drawContours(img, [contour], -1, (0, 0, 255), 2)


# 이미지 외곽선에 대한 모든좌표를 전부 리턴하기 때문에 필요한 값만 가져와야함.
pt1 = np.float32([[0, 0],[0, 0],[0, 0],[0, 0]])
pt2 = np.float32([[0, 0], [0, img.shape[0]], [img.shape[1], img.shape[0]], [img.shape[1], 0]])
# left_top, left_bottom, right_bottom, right_top

# 이미지 4좌표 구하기
buffer = []
for idx, xy in enumerate(c_data):
    if idx == 0:
        pt1[0] = xy
        buffer = xy
    elif idx == len(c_data)-1:
        pt1[3] = xy
    elif xy[0] - buffer[0] > 100:
        pt1[2] = xy
        pt1[1] = buffer
        buffer = xy
    else:
        buffer = xy

M = cv2.getPerspectiveTransform(pt1, pt2)
dst = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))

cv2.imshow('dst', dst)
cv2.imwrite('D:/github/OpenCV-Python/2022-10-25/test.png', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
