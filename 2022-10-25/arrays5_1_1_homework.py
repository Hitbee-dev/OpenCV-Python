import cv2
import matplotlib.pyplot as plt

image = cv2.imread('D:/github/OpenCV-Python/2022-10-11/images/test_image.jpg', cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(3,4))
plt.title('original_image')
plt.axis('off')
plt.imshow(image)

titles = ['x_axis', 'y_axis', 'xy_axis', 'trans_image']
flip_images = [cv2.flip(image, 0), cv2.flip(image, 1), cv2.flip(image, -1), cv2.transpose(image)]

plt.figure(figsize=(6,8))
plt.suptitle('image flip')
for idx, (title, flip_image) in enumerate(zip(titles, flip_images)):
    plt.subplot(2, 2, idx+1) # 2행 2열의 이미지 순서
    plt.title(f'{title}')
    plt.axis('off')
    plt.imshow(flip_image)
plt.show()