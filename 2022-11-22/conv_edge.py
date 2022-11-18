import numpy as np, cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:/github/OpenCV-Python/2022-11-22/images/hue_image.jpg', cv2.IMREAD_COLOR)

# 이미지 그레이 스케일 변환
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# sobel vertical(수직)
sobel_v_mask = np.array([[-1, 0, 1],
                         [-2, 0, 2], 
                         [-1, 0, 1]], dtype=float)
sobel_v_img = cv2.filter2D(img, cv2.CV_16S, sobel_v_mask)
sobel_v_img = cv2.convertScaleAbs(sobel_v_img)

# sobel horizontal(수평)
sobel_h_mask = np.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]], dtype=float)
sobel_h_img = cv2.filter2D(img, cv2.CV_16S, sobel_h_mask)
sobel_h_img = cv2.convertScaleAbs(sobel_h_img)

sobel_img = cv2.addWeighted(sobel_v_img, 0.5, sobel_h_img, 0.5, 0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# sobel vertical(수직)
sobel_v_mask2 = cv2.Sobel(img, cv2.CV_16S, 1, 0)
sobel_v_img2 = cv2.convertScaleAbs(sobel_v_mask2)

# sobel horizontal(수평)
sobel_h_mask2 = cv2.Sobel(img, cv2.CV_16S, 0, 1)
sobel_h_img2 = cv2.convertScaleAbs(sobel_h_mask2)

sobel_img2 = cv2.addWeighted(sobel_v_img2, 0.5, sobel_h_img2, 0.5, 0)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# laplacian edge image
laplacian_img = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
laplacian_img = cv2.convertScaleAbs(laplacian_img)

# log edge image
gaus_mask = cv2.GaussianBlur(img, (3, 3), 0, 0)
log_img = cv2.Laplacian(gaus_mask, cv2.CV_16S, 3).astype(np.uint8)

# dog edge image
gaus2_mask = cv2.GaussianBlur(img, (9, 9), 0, 0)
dog_img = gaus_mask - gaus2_mask

# canny edge image
canny_img = cv2.Canny(img, 400, 200)

# minmax filter function
def minmax_filter(image, ksize, mode):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            mask = image[y1:y2, x1:x2]
            dst[i, j] = cv2.minMaxLoc(mask)[mode]
    return dst

# min filter image
min_img = cv2.erode(img, np.ones((3, 3), np.uint8), iterations=1)

# minfilter image
minfilter_img = minmax_filter(img, 3, 0) # 최솟값 필터링

# max filter image
max_img = cv2.dilate(img, np.ones((3, 3), np.uint8), iterations=1)

# maxfilter image
maxfilter_img = minmax_filter(img, 3, 1) # 최댓값 필터링

# mean filter function
def mean_filter(image, ksize):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    center = ksize // 2

    for i in range(rows):
        for j in range(cols):
            y1, y2 = i - center, i + center + 1
            x1, x2 = j - center, j + center + 1
            if y1 < 0 or y2 > rows or x1 < 0 or x2 > cols:
                dst[i, j] = image[i, j]
            else:    
                mask = image[y1:y2, x1:x2]
                dst[i, j] = np.mean(mask)
    return dst

# meanfilter image
meanfilter_img = mean_filter(img, 3)

# mean filter image
mean_img = cv2.blur(img, (3, 3))

# median filter image
median_img = cv2.medianBlur(img, 3)

plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(30, 8))

pltx, plty = 7, 2
titles = ['img', 'blur_img', 'sharp_img', 'roberts_img', 'prewitt_img', 'sobel_img2', 'laplacian_img', 'log_img', 'dog_img', 'canny_img', 'min_img', 'max_img', 'mean_img', 'median_img']
for idx, title in enumerate(titles):
    plt.subplot(plty, pltx, idx+1)
    plt.axis('off')
    plt.title(title)
    plt.imshow(eval(title), aspect='auto', cmap='gray')

plt.show()
cv2.waitKey(0)