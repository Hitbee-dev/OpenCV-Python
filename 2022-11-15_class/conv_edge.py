import numpy as np, cv2
import matplotlib.pyplot as plt

img = cv2.imread('images/hue_image.jpg', cv2.IMREAD_COLOR)

# 이미지 그레이 스케일 변환
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', img)

# blur
blur_mask = np.array([[1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9],
                      [1/9, 1/9, 1/9]], dtype=float)
blur_img = cv2.filter2D(img, cv2.CV_16S, blur_mask) # 마스크를 적용하는 함수
blur_img = cv2.convertScaleAbs(blur_img)

# sharp
sharp_mask = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]], dtype=float)
sharp_img = cv2.filter2D(img, cv2.CV_16S, sharp_mask)
sharp_img = cv2.convertScaleAbs(sharp_img)

# roberts left -> right
roberts_lr_mask = np.array([[-1, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]], dtype=float)
roberts_lr_img = cv2.filter2D(img, cv2.CV_16S, roberts_lr_mask)
roberts_lr_img = cv2.convertScaleAbs(roberts_lr_img)

# roberts right -> left
roberts_rl_mask = np.array([[0, 0, -1],
                            [0, 1, 0],
                            [0, 0, 0]], dtype=float)
roberts_rl_img = cv2.filter2D(img, cv2.CV_16S, roberts_rl_mask)
roberts_rl_img = cv2.convertScaleAbs(roberts_rl_img)

roberts_img = cv2.addWeighted(roberts_lr_img, 0.5, roberts_rl_img, 0.5, 0)
# cv2.magnitude(roberts_lr_img, roberts_rl_img)
# np.clip()

# prewitt vertical(수직)
prewitt_v_mask = np.array([[-1, 0, 1],
                            [-1, 0, 1],
                            [-1, 0, 1]], dtype=float)
prewitt_v_img = cv2.filter2D(img, cv2.CV_16S, prewitt_v_mask)
prewitt_v_img = cv2.convertScaleAbs(prewitt_v_img)

# prewitt horizontal(수평)
prewitt_h_mask = np.array([[-1, -1, -1],
                            [0, 0, 0],
                            [1, 1, 1]], dtype=float)
prewitt_h_img = cv2.filter2D(img, cv2.CV_16S, prewitt_h_mask)
prewitt_h_img = cv2.convertScaleAbs(prewitt_h_img)

prewitt_img = cv2.addWeighted(prewitt_v_img, 0.5, prewitt_h_img, 0.5, 0)










plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(8, 12))

pltx, plty = 2, 4
titles = ['blur_img', 'sharp_img', 'roberts_img', 'prewitt_img']
for idx, title in enumerate(titles):
    plt.subplot(plty, pltx, idx+1)
    plt.axis('off')
    plt.title(title)
    plt.imshow(eval(title), aspect='auto', cmap='gray')

plt.show()
cv2.waitKey(0)