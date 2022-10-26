import numpy as np, cv2

image = cv2.imread('D:/github/OpenCV-Python/2022-10-18/images/dark_image.png', cv2.IMREAD_GRAYSCALE)

min_val, max_val, _, _ = cv2.minMaxLoc(image)
# 최소값과 최대값 가져오기

ratio = 255 / (max_val - min_val)
dst = np.round((image - min_val) * ratio).astype('uint8')
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

print(f'원본 영상 최솟값 = {min_val}, 최댓값 = {max_val}')
print(f'수정 영상 최솟값 = {min_dst}, 최댓값 = {max_dst}')
cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)