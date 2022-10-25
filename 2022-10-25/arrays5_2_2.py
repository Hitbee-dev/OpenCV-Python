import cv2
import matplotlib.pyplot as plt

image = cv2.imread('D:/github/OpenCV-Python/2022-10-11/images/test_image.jpg', cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
red, green, blue = cv2.split(image)
'''
plt.subplot(2, 2, 1) # 2행 2열의 1번째 이미지
plt.title('original')
plt.axis('off')
plt.imshow(image, cmap=None)

plt.subplot(2, 2, 2) # 2행 2열의 2번째 이미지
plt.title('red')
plt.axis('off')
plt.imshow(red, cmap='gray')

plt.subplot(2, 2, 3) # 2행 2열의 3번째 이미지
plt.title('green')
plt.axis('off')
plt.imshow(green, cmap='gray')

plt.subplot(2, 2, 4) # 2행 2열의 4번째 이미지
plt.title('blue')
plt.axis('off')
plt.imshow(blue, cmap='gray')
'''
# 반복해서 깔끔하게 코드짜는 방법

titles = ['original', 'red', 'green', 'blue']
images = [image, red, green, blue]
cmaps = [None, 'gray', 'gray', 'gray']

for idx, (title, img, c) in enumerate(zip(titles, images, cmaps)):
    plt.subplot(2, 2, idx+1) # 2행 2열의 이미지 순서
    plt.title(title)
    plt.axis('off')
    plt.imshow(img, cmap=c)

plt.show()