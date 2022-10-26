import numpy as np, cv2

bg_img = cv2.imread('D:/github/OpenCV-Python/2022-10-18/images/background.jpg', cv2.IMREAD_COLOR)
icon_img = cv2.imread('D:/github/OpenCV-Python/2022-10-18/images/python_logo.png', cv2.IMREAD_COLOR)

print(bg_img.shape, icon_img.shape)
icon_img = cv2.resize(icon_img, dsize=(icon_img.shape[1]//16, icon_img.shape[0]//16))
# background 이미지에 icon 이미지를 입힐거라, icon 이미지가 더 작아야하기 때문에 사이즈 조절
print(icon_img.shape)
cv2.imshow('icon_img', icon_img)

ret, masks = cv2.threshold(icon_img, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', masks)

masks = cv2.split(masks)
cv2.imshow('mask0', masks[0]) # 단색 (파랑 B)
cv2.imshow('mask1', masks[1]) # 단색 (노랑의 G)
cv2.imshow('mask2', masks[2]) # 단색 (노랑의 R)
# 노란색은 R G B 기준으로 R과 G로 만들 수 있다.

fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
cv2.imshow('fg_mask', fg_pass_mask)

fg_pass_mask = cv2.bitwise_or(masks[2],fg_pass_mask)
cv2.imshow('fg_mask2', fg_pass_mask)

bg_pass_mask = cv2.bitwise_not(fg_pass_mask)
cv2.imshow('bg_mask', bg_pass_mask)

## 관심영역 지정 (중심 좌표 구하기)
(H, W), (h, w) = bg_img.shape[:2], icon_img.shape[:2]
x, y = (W-w)//2, (H-h)//2
roi = bg_img[y:y+h, x:x+w]
cv2.imshow('roi', roi)

# 행렬 논리곱과 마스킹을 이용한 관심 영역 복사
foreground = cv2.bitwise_and(icon_img, icon_img, mask=fg_pass_mask)
cv2.imshow('foreground', foreground)

background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)
cv2.imshow('background', background)

dst = cv2.add(background, foreground)
cv2.imshow('dst', dst)

bg_img[y:y+h, x:x+w] = dst
cv2.imshow('origin_img', bg_img)
cv2.waitKey(0)