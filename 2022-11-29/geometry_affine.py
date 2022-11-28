# 어핀 변환이라고도 하고, 어파인 변환이라고도 함.
# 비례를 유지하는 기하학적 함수
# 어파인 변환은 크기가 2x3이어야 함.

'''
OpenCV에서 제공하는 어파인 변환: cv2.warpAffine()
어파인 변환 행렬을 만드는 합수: cv2.getAffineTransform(), cv2.getRotationMatrix2D()

cv2.getAffineTransform()
함수는 변환 전 좌표 3개와 변환 후 좌표 3개를 지정하면 해당 변환을 수행해 줄 수 있는
어파인 행렬을 반환한다.

cv2.getRotationMatrix2D()
함수는 회전 변환과 크기 변경을 수행하는
어파인 행렬을 반환한다.

회전의 방향은 양수일 때 반시계 방향으로 회전하는 행렬을 반환한다.
-> 영상 좌표 직교 좌표계에서의 회전과 같은 방향으로 표현하기 위함이다.
'''
import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-29/images/opencv_icon.png", cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
h, w, c = image.shape

'어파인 변환을 활용한 이동'
a, b = -100, 200
mov_M = np.array([[1, 0, a],
                  [0, 1, b]], dtype=np.float32)
# x축으로 100, y축으로 200 이동
image_move = cv2.warpAffine(image, mov_M, (w, h))

'어파인 변환을 활용한 회전'
# center = (w // 2, h // 2)
# scale = 0.7
# angle = 45
# rot_M = cv2.getRotationMatrix2D(center, angle, scale)
# image_rotate = cv2.warpAffine(image, rot_M, (w, h))
center = (w // 2, h // 2)
scale = 0.7
angle = 45
theta = np.radians(angle)
alpha = scale * np.cos(theta)
beta = scale * np.sin(theta)
rot_M = np.array([[alpha, beta, (1-alpha)*center[0] - beta*center[1]],
                  [-beta, alpha, beta*center[0] + (1-alpha)*center[1]]], dtype=np.float32)
image_rotate = cv2.warpAffine(image, rot_M, (w, h))

'어파인 변환을 이용한 크기 변환'
# 회전을 하면서 scale값을 변경하여 크기를 한번에 바꿀 수도 있지만, 따로 변환도 가능하다.
# 방법1
resize_M = cv2.getRotationMatrix2D(center, 0, 0.5)
image_resize = cv2.warpAffine(image, resize_M, (w, h))

# 방법2
# s_x, s_y = 0.5, 0.5
# resize_M = np.array([[s_x, 0, 0],
#                      [0, s_y, 0]], dtype=np.float32)
# image_resize = cv2.warpAffine(image, resize_M, (w, h))

# 방법3
# image_resize = np.zeros((h, w, c), dtype=np.uint8)
# resize_M = cv2.resize(image, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# image_resize[:resize_M.shape[0], :resize_M.shape[1]] = resize_M

'matplotlib을 이용해 한번에 출력'
titles = ['image', 'image_move', 'image_rotate', 'image_resize']
plt.figure(figsize=(12, 10))
for idx, title in enumerate(titles):
    plt.subplot(2, 2, idx+1)
    plt.axis("off")
    plt.title(title)
    plt.imshow(eval(title))
plt.show()