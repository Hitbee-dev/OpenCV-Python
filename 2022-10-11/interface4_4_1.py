import cv2

image_file_path = 'D:/github/OpenCV-Python/2022-10-04/images/test_image.jpg'

title1, title2 = 'cv2gray', 'cv2color'
cv2gray = cv2.imread(image_file_path, cv2.IMREAD_GRAYSCALE)
cv2color = cv2.imread(image_file_path, cv2.IMREAD_COLOR)

cv2.imshow(title1, cv2gray)
cv2.imshow(title2, cv2color)
cv2.waitKey(0)
cv2.destroyAllWindows()