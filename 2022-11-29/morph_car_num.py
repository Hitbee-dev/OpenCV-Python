import numpy as np, cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-11-29/images/car_image.jpg", cv2.IMREAD_COLOR)

mask = np.ones((5, 17), np.uint8)
# 번호판의 가로 세로 비율이 약 17:5므로 17x5 크기의 마스크를 생성
# numpy의 행렬은 반대로 적용되기 때문에 (5, 17)의 1로 채워진 마스크를 생성
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 원본 이미지를 그레이 스케일로 변환
blur = cv2.blur(gray, (5, 5))
# 잡음 제거를 위한 블러링 처리
# 여기서 5, 5는 5 x 5범위 내 이웃 픽셀을 평균으로, 블러링 처리하는 것이다.
sobel = cv2.Sobel(blur, cv2.CV_8U, 1, 0, 5)
# Sobel 함수를 이용하여 수직 방향의 에지를 검출
'''
1. gray는 입력 이미지
2. cv2.CV_8U는 8비트 부호 없는 정수형(Unsigned int)을 의미
3. 1은 dx로, x방향 미분 차수를 의미
4. 0은 dy로, y방향 미분 차수를 의미
5. 5는 ksize로, 소벨 커널의 크기를 의미

cv2.Sobel(gray, cv2.CV_8U, 1, 0, 5) = 수직 방향의 에지를 검출
cv2.Sobel(gray, cv2.CV_8U, 0, 1, 5) = 수평 방향의 에지를 검출
'''
# 수직 방향의 에지를 검출한 후, 모폴로지 닫힘 연산을 진행하면 주변 픽셀을 참조하여 픽셀의 값을 결정함.
# 그 결과는 이미지를 보면 쉽게 이해할 수 있다.

ret, thresh = cv2.threshold(sobel, 120, 255, cv2.THRESH_BINARY)
# ret = 임계값, thresh = 임계값을 적용한 결과
'''
1. gray는 입력 이미지
2. 120은 임계 값
3. 255는 최대 값 (이미지는 0 ~ 255로 이루어져 있기 때문에 최대값을 255로 주면 된다.)
4. cv2.THRESH_BINARY는 임계값을 넘으면 최대값으로, 넘지 못하면 0으로 처리
'''
morph_close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, mask, iterations=3)
# 모폴로지 닫힘 연산
'''
1. thresh는 입력 이미지
2. cv2.MORPH_CLOSE는 모폴로지 연산 종류(열림 또는 닫힘)
3. mask는 앞에서 설정한 마스킹 범위 (번호판에 해당하는 예상 범위)
4. iterations는 반복 횟수 (너무 적어도, 너무 많아도 이상하게 나온다.)
'''

titles = ['image', 'gray', 'blur', 'sobel', 'thresh', 'morph_close']

plt.figure(figsize=(12, 10))

for idx, title in enumerate(titles):
    plt.subplot(3, 2, idx+1)
    plt.axis("off")
    plt.title(title)
    plt.imshow(eval(title), cmap="gray")

plt.show()
