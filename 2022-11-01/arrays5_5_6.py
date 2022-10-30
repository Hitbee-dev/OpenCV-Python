import numpy as np, cv2

image = np.full((400, 500, 3), 255, np.uint8)
theta = 45 * np.pi / 180 # 45도 회전

m = np.array([[np.cos(theta), -np.sin(theta), 0],
              [np.sin(theta), np.cos(theta), 0],
              [0, 0, 1]], np.float32)

pts1 = np.array([(200, 50, 1), (400, 50, 1),
                 (400, 250, 1), (200, 250, 1)], np.float32)
############################################################################################################

delta = (pts1[2] - pts1[0])//2 # 시작좌표와 종료좌표 차분//2
center = pts1[0] + delta       # 중심 좌표 계산

pts2 = cv2.gemm(pts1, m, 1.0, None, 1.0, flags = cv2.GEMM_2_T) # 이미지 회전
delta2 = (pts2[2] - pts2[0])//2 # 시작좌표와 종료좌표 차분//2
center2 = pts2[0] + delta2       # 중심 좌표 계산

t1 = center[0] - center2[0]
t2 = center[1] - center2[1]

m2 = np.array([[np.cos(theta), -np.sin(theta), t1],
              [np.sin(theta), np.cos(theta), t2],
              [0, 0, 1]], np.float32)
print(m2)
############################################################################################################
pts3 = cv2.gemm(pts1, m2, 1.0, None, 1.0, flags = cv2.GEMM_2_T) # 이미지 회전

cv2.polylines(image, [np.int32(pts1[:, :2])], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2[:, :2])], True, (255, 0, 0), 2)
cv2.polylines(image, [np.int32(pts3[:, :2])], True, (0, 0, 255), 2)
cv2.imshow('image', image)
cv2.waitKey(0)