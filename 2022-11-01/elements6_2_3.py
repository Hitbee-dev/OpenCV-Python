import matplotlib.pyplot as plt, cv2

image = cv2.imread('D:/github/OpenCV-Python/2022-11-01/images/background.jpg', cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# opencv함수 이용(saturation 방식)
dst1 = cv2.add(image, 100)
dst2 = cv2.subtract(image, 100)

# numpy함수 이용(modulo 방식)
dst3 = image + 100
dst4 = image - 100

plt.figure(figsize=(5, 4))
plt.title('origin_image')
plt.axis('off')
plt.imshow(image, cmap='gray')

titles = ['dst1', 'dst2', 'dst3', 'dst4']
plt.figure(figsize=(10, 8))
for idx, title in enumerate(titles):
    plt.subplot(2, 2, idx+1)
    plt.title(title)
    plt.axis('off')
    plt.imshow(eval(title), cmap='gray')
plt.show()