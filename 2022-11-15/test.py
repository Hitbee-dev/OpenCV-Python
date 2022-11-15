# 2022-11-15, multimedia information processing practice
import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_edge(image, data1, data2):
    dst1 = cv2.filter2D(image, cv2.CV_32F, data1)
    dst2 = cv2.filter2D(image, cv2.CV_32F, data2)
    dst = cv2.magnitude(dst1, dst2)
#    return dst
#    return cv2.convertScaleAbs(dst)
    return np.clip(dst, 0, 255).astype('uint8')

image = cv2.imread("D:/github/OpenCV-Python/2022-11-15/images/hue_image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상 파일 읽기 오류")

blur = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]], dtype=float)
blur_image = cv2.filter2D(image, cv2.CV_32F, blur)

sharp = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=float)
sharp_image = cv2.filter2D(image, cv2.CV_32F, sharp)

# roberts edge
data1 = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 0]], dtype=float)
data2 = np.array([[0, 0, -1], [0, 1, 0], [0, 0, 0]], dtype=float)
roberts_image = get_edge(image, data1, data2)

#  prewit edge
data1 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=float)
data2 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=float)
prewitt_image = get_edge(image, data1, data2)

# sobel
sobel_x = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)
sobel_y = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)
# sobel_image = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0).astype('uint8')
sobel_image = cv2.magnitude(sobel_x, sobel_y)
sobel_image = np.clip(sobel_image, 0, 255).astype('uint8')

# sobel_image = cv2.add(sobel_image, 0, cv2.CV_8U)
# sobel_image = cv2.normalize(sobel_grad, 0, 255, cv2.NORM_MINMAX).astype('uint8')

lap_image = cv2.Laplacian(image, cv2.CV_16S, 1)
lap_image = cv2.normalize(lap_image, 0, 255, cv2.NORM_MINMAX).astype('uint8')
# lap_image = cv2.convertScaleAbs(lap_image)

gaus = cv2.GaussianBlur(image, (7,7), 0, 0)
log_image = cv2.Laplacian(gaus, cv2.CV_32F, 7)
log_image = cv2.normalize(log_image, 0, 255, cv2.NORM_MINMAX).astype('uint8')
# lap_image = cv2.convertScaleAbs(log_image)

gaus1 = cv2.GaussianBlur(image, (3,3), 0, 0)
gaus2 = cv2.GaussianBlur(image, (5,5), 0, 0)
dog_image = gaus1 - gaus2
dog_image = cv2.normalize(dog_image, 0, 255, cv2.NORM_MINMAX).astype('uint8')

res_images = [ "image", "blur_image", "sharp_image", "roberts_image", "prewitt_image",
           "sobel_image", "lap_image", "log_image", "dog_image"]
res_title = [ "Original", "Blurring filter", "Sharpening filter", "Roberts edge", "Prewitt edge",
           "Sobel edge", "Laplacian edge", "LoG edge", "DoG edge"]

plt.rcParams['toolbar'] = 'None'
fig = plt.figure(frameon=False, figsize=(8,8))
#fig = plt.figure(figsize=(8,8))
for sfig in range(9):
    plt.subplot(3,3,sfig+1)
    plt.imshow(eval(res_images[sfig]), aspect='auto', cmap='gray')
    plt.axis('off')
    plt.title(res_title[sfig])

plt.suptitle('Comparison of various spatial operations')
#fig.canvas.toolbar.pack_forget()
plt.show()