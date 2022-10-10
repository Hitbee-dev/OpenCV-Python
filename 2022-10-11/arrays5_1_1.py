import cv2

image = cv2.imread('D:/github/OpenCV-Python/2022-10-11/images/test_image.jpg', cv2.IMREAD_COLOR)

x_axis = cv2.flip(image, 0)
y_axis = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)
trans_image = cv2.transpose(image)

titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'trans_image']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)