import cv2

image_file_path = 'D:/github/OpenCV-Python/2022-10-04/images/test_image.jpg'
save_file_path = 'D:/github/OpenCV-Python/2022-10-04/save_images/'

image = cv2.imread(image_file_path, cv2.IMREAD_COLOR)

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)     # JPEG 화질 설정
params_png = (cv2.IMWRITE_PNG_COMPRESSION, 9)   # PNG 압축율 설정

cv2.imwrite(f'{save_file_path}write_test1.jpg', image)
cv2.imwrite(f'{save_file_path}write_test2.jpg', image, params_jpg)
cv2.imwrite(f'{save_file_path}write_test3.png', image)
cv2.imwrite(f'{save_file_path}write_test4.png', image, params_png)

print('저장 완료')