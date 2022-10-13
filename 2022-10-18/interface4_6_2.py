import cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-10-11/images/test_image.jpg", cv2.IMREAD_COLOR)

rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(6,4))
plt.suptitle('figure2- pyplot image display')
plt.subplot(1, 2, 1) # 1행 2열의 첫번째 이미지
plt.title('rgb_image')
plt.axis('off')
plt.imshow(rgb_img)

plt.subplot(1, 2, 2) # 1행 2열의 두번째 이미지
plt.title('gray_image')
plt.imshow(gray_img, cmap='gray')
plt.show()
