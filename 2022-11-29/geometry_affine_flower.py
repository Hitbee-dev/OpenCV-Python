import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-29/images/flower.png", cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, c = image.shape

pt1 = np.array([[772, 196], [1190, 824], [443, 962]], np.float32)
# 원본 이미지에서 이미지를 변환할 좌표 설정
pt2 = np.array([[275, 503], [1286, 128], [1332, 893]], np.float32)
# 변환된 이미지의 좌표 설정
for pt in pt1:
    cv2.circle(image, tuple(pt.astype(int)), 10, (255, 0, 0), 5)
    '''
    1. 입력 영상
    2. 원의 중심 좌표
    3. 원의 반지름
    4. 원의 색상
    5. 원의 두께
    '''
aff_mat = cv2.getAffineTransform(pt1, pt2)
affine = cv2.warpAffine(image, aff_mat, (w, h))

titles = ["image", "affine"]
plt.figure(figsize=(12, 6))
for idx, title in enumerate(titles):
    plt.subplot(1, 2, idx+1)
    plt.axis("off")
    plt.title(title)
    plt.imshow(eval(title))
plt.show()