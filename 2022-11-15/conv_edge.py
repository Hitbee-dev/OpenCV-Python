import numpy as np, cv2
import matplotlib.pyplot as plt

# original image
img = cv2.imread("D:/github/OpenCV-Python/2022-11-15/images/hue_image.jpg", cv2.IMREAD_COLOR)

# matplotlib, gray scale
img =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# original image
cv2.imshow("original", img)

# blur convolution image
blur_mask = [1/9, 1/9, 1/9,
             1/9, 1/9, 1/9,
             1/9, 1/9, 1/9]
blur_mask = np.array(blur_mask, np.float32).reshape(3, 3)
blur_img = cv2.filter2D(img, cv2.CV_16S, blur_mask)
blur_img = cv2.convertScaleAbs(blur_img)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# sharp convolution image
sharp_mask = [0, -1, 0,
              -1, 5, -1,
              0, -1, 0]
sharp_mask = np.array(sharp_mask, np.float32).reshape(3, 3)
sharp_img = cv2.filter2D(img, cv2.CV_16S, sharp_mask)
sharp_img = cv2.convertScaleAbs(sharp_img)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# roberts left -> right edge image
roberts_lr_mask = [-1, 0, 0,
                    0, 1, 0,
                    0, 0, 0]
roberts_lr_mask = np.array(roberts_lr_mask, np.float32).reshape(3, 3)
roberts_lr_img = cv2.filter2D(img, cv2.CV_16S, roberts_lr_mask)
roberts_lr_img = cv2.convertScaleAbs(roberts_lr_img)

# roberts right -> left edge image
roberts_rl_mask = [0, 0, -1,
                   0, 1, 0,
                   0, 0, 0]
roberts_rl_mask = np.array(roberts_rl_mask, np.float32).reshape(3, 3)
roberts_rl_img = cv2.filter2D(img, cv2.CV_16S, roberts_rl_mask)
roberts_rl_img = cv2.convertScaleAbs(roberts_rl_img)

# roberts merge edge image
roberts_img = cv2.addWeighted(roberts_lr_img, 0.5, roberts_rl_img, 0.5, 0)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# prewitt vertical edge image
prewitt_v_mask = [-1, 0, 1,
                  -1, 0, 1,
                  -1, 0, 1]
prewitt_v_mask = np.array(prewitt_v_mask, np.float32).reshape(3, 3)
prewitt_v_img = cv2.filter2D(img, cv2.CV_16S, prewitt_v_mask)
prewitt_v_img = cv2.convertScaleAbs(prewitt_v_img)

# prewitt horizontal edge image
prewitt_h_mask = [-1, -1, -1,
                    0, 0, 0,
                    1, 1, 1]
prewitt_h_mask = np.array(prewitt_h_mask, np.float32).reshape(3, 3)
prewitt_h_img = cv2.filter2D(img, cv2.CV_16S, prewitt_h_mask)
prewitt_h_img = cv2.convertScaleAbs(prewitt_h_img)

# prewitt merge edge image
prewitt_img = cv2.addWeighted(prewitt_v_img, 0.5, prewitt_h_img, 0.5, 0)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# sobel vertical edge image
sobel_v_mask = [-1, 0, 1,
                -2, 0, 2,   
                -1, 0, 1]
sobel_v_mask = np.array(sobel_v_mask, np.float32).reshape(3, 3)
sobel_v_img = cv2.filter2D(img, cv2.CV_16S, sobel_v_mask)
sobel_v_img = cv2.convertScaleAbs(sobel_v_img)

# sobel horizontal edge image
sobel_h_mask = [-1, -2, -1,
                  0, 0, 0,
                  1, 2, 1]
sobel_h_mask = np.array(sobel_h_mask, np.float32).reshape(3, 3)
sobel_h_img = cv2.filter2D(img, cv2.CV_16S, sobel_h_mask)
sobel_h_img = cv2.convertScaleAbs(sobel_h_img)

# sobel merge edge image
sobel_img = cv2.addWeighted(sobel_v_img, 0.5, sobel_h_img, 0.5, 0)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# laplacian 4point edge image
laplacian_4p_mask = [ 0, 1, 0,
                     1, -4, 1,
                      0, 1, 0]
laplacian_4p_mask = np.array(laplacian_4p_mask, np.int16).reshape(3, 3) # 음수로 인해 int16 행렬 선언
laplacian_4p_img = cv2.filter2D(img, cv2.CV_16S, laplacian_4p_mask)
laplacian_4p_img = cv2.convertScaleAbs(laplacian_4p_img)

# laplacian 8point edge image
laplacian_8p_mask = [-1, -1, -1,
                     -1, 8, -1,  
                     -1, -1, -1]
laplacian_8p_mask = np.array(laplacian_8p_mask, np.int16).reshape(3, 3) # 음수로 인해 int16 행렬 선언
laplacian_8p_img = cv2.filter2D(img, cv2.CV_16S, laplacian_8p_mask)
laplacian_8p_img = cv2.convertScaleAbs(laplacian_8p_img)

# laplacian merge edge image
laplacian_img = cv2.addWeighted(laplacian_4p_img, 0.5, laplacian_8p_img, 0.5, 0)

laplacian_img = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
laplacian_img = cv2.convertScaleAbs(laplacian_img)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# log edge image
gaus_mask = cv2.GaussianBlur(img, (3, 3), 0, 0)
log_img = cv2.Laplacian(gaus_mask, cv2.CV_16S, 3).astype(np.uint8)

# dog edge image
gaus2_mask = cv2.GaussianBlur(img, (9, 9), 0, 0)
dog_img = gaus_mask - gaus2_mask

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''
plt.figure(figsize=(20, 8))

pltx, plty = 5, 2
titles = [  'blur_img', 'sharp_img',
            'roberts_lr_img', 'roberts_rl_img',
            'prewitt_v_img', 'prewitt_h_img',
            'sobel_v_img', 'sobel_h_img',
            'laplacian_4p_img', 'laplacian_8p_img'  ]

for idx, title in enumerate(titles):
    plt.subplot(plty, pltx, idx+1)
    plt.axis('off')
    plt.title(title)
    plt.imshow(eval(title), cmap='gray')
'''
cv2.imshow("dog_img", dog_img)
# '''
plt.figure(figsize=(12, 12))

pltx, plty = 2, 4
titles = ['blur_img', 'sharp_img', 'roberts_img', 'prewitt_img', 'sobel_img', 'laplacian_img', 'log_img', 'dog_img']
for idx, title in enumerate(titles):
    plt.subplot(plty, pltx, idx+1)
    plt.axis('off')
    plt.title(title)
    plt.imshow(eval(title), cmap='gray')
# '''
plt.show()

cv2.waitKey(0)