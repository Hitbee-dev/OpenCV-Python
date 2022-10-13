import cv2
import matplotlib.pyplot as plt

image = cv2.imread("D:/github/OpenCV-Python/2022-10-11/images/test_image.jpg", cv2.IMREAD_COLOR)

print(image.shape)

plt.figure(figsize=(3,4))
plt.imshow(image)
plt.title('figure2- original(bgr)')
plt.axis('off')
plt.show()