# 어핀 변환이라고도 하고, 어파인 변환이라고도 함.
# 비례를 유지하는 기하학적 함수

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
'''
image = cv2.imread("D:/github/OpenCV-Python/2022-11-29/images/opencv_icon.png", cv2.IMREAD_GRAYSCALE)

size = image.shape[::-1]                            # 영상 크기(y, x) -> (x, y)
center = np.divmod(size, 2)[0]                      # divmod = 몫과 나머지를 반환하는 함수,
                                                    # 뒤에 있는 값으로 앞에 있는 값을 나눔
center = (image.shape[1] // 2, image.shape[0] // 2) # 회전 변환 기준 좌표(영상 중심), 이렇게 구현해도 됨
angle = 45                                          # 회전 각도(30도), 
tr = (200, 0)                                       # 평행이동 값 지정
scale = 0.65                                        # 크기 변경 비율 지정

print(size, center)

pt1 = np.array([(462, 173),(658, 509),(269, 514)], np.float32)
pt2 = np.array([(642, 73),(638, 389),(229, 794)], np.float32)
aff_mat = cv2.getAffineTransform(pt1, pt2)
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)

dst1 = cv2.warpAffine(image, aff_mat, size)
dst2 = cv2.warpAffine(image, rot_mat, size)
cv2.imwrite("D:/github/OpenCV-Python/2022-11-29/images/opencv_img.png", dst2)

cv2.imshow('image', image)
cv2.imshow('affine', dst1)
cv2.imshow('rotation', dst2)
cv2.waitKey(0)
'''

image = cv2.imread("D:/github/OpenCV-Python/2022-11-29/images/opencv_icon.png", cv2.IMREAD_COLOR)
cv2.imshow('image', image)
h, w, c = image.shape

'어파인 변환을 활용한 회전'
center = (w // 2, h // 2)
angle = 45
scale = 1
rot_M = cv2.getRotationMatrix2D(center, angle, scale)
dst1 = cv2.warpAffine(image, rot_M, (w, h))
cv2.imshow("dst1", dst1)

'어파인 변환을 활용한 이동'
M = np.array([[1, 0, -100],
              [0, 1, 200]], dtype=np.float32)
# x축으로 100, y축으로 200 이동

dst2 = cv2.warpAffine(image, M, (w, h))
cv2.imshow('dst2', dst2)

'어파인 변환을 이용한 크기 변환'



'matplotlib을 이용해 한번에 출력'
cv2.waitKey(0)
