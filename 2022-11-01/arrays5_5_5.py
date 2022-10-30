import numpy as np, cv2

image = np.full((400, 500, 3), 255, np.uint8)
theta = 20 * np.pi / 180 # 회전할 라디안 각도 계산


pts1 = np.array([
    (250, 30), (400, 70), (350, 250), (150, 200)
    # left_top, right_top, right_bottom, left_bottom
    ], np.float32)

rot_mat = np.array([
    [np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]
    ], np.float32)
pts2 = cv2.gemm(pts1, rot_mat, 1.0, None, 1.0, flags = cv2.GEMM_2_T)

cv2.polylines(image, [np.int32(pts1)], True, (0, 255, 0), 2)
cv2.polylines(image, [np.int32(pts2)], True, (255, 0, 0), 3)
cv2.imshow('image', image)
cv2.waitKey(0)