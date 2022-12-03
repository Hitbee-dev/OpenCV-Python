import numpy as np, cv2, math
import matplotlib.pyplot as plt

def draw_hough_lines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    min_length = min(len(lines), nline)

    for i in range(min_length):
        # 수직거리, 각도
        rho, radian = lines[i, 0, 0:2]
        a, b = math.cos(radian), math.sin(radian)

        # 직선 위 2개 좌표 계산
        pt = (a * rho, b * rho)

        # 직선상의 이동 위치
        delta = (-1000 * b, 1000 * a)
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (255, 0, 0), 2, cv2.LINE_AA)
    
    return dst

# 이미지 읽기
image = cv2.imread("D:/github/OpenCV-Python/2022-12-06/images/hough.png", cv2.IMREAD_GRAYSCALE)

# 가우시안 블러링
blur = cv2.GaussianBlur(image, (5, 5), 2, 2)

# 캐니 엣지 검출
canny = cv2.Canny(blur, 100, 200, 5)

# 수직거리 간격, 각도 간격
rho, theta = 1, np.pi / 180

# 허프 변환 직선 검출
lines = cv2.HoughLines(canny, rho, theta, 20)

# 직선 그리기
dst = draw_hough_lines(image, lines, 7)

# 반복문으로 이미지 한번에 출력
titles = ['image', 'canny', 'dst']
plt.figure(figsize=(6, 10))
for idx, title in enumerate(titles):
    plt.subplot(3, 1, idx+1)
    plt.axis("off")
    plt.title(title)
    plt.imshow(eval(title), cmap='gray')
plt.show()