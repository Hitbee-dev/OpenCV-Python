import matplotlib.pyplot as plt, cv2

image = cv2.imread('D:/github/OpenCV-Python/2022-11-01/images/background.jpg', cv2.IMREAD_COLOR)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(x1, y1), (x2, y2) = (276, 25), (317, 51)
(x, y), (w, h) = (276, 25), (x2-x1, y2-y1)

roi_img = image[y:y+h, x:x+w]

for row in roi_img:
    for p in row:
        print("%4d" % p , end=' ')
    print()

cv2.rectangle(image, (x, y, w, h), 255, 1)
plt.figure(figsize= (10, 4))
plt.subplot(1, 2, 1)
plt.axis('off')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.imshow(roi_img, cmap='gray')
plt.axis('off')
plt.show()