import cv2

capture = cv2.VideoCapture(0)

fps = 29.97
delay = round(1000/fps)
size = (640, 360)
fourcc = cv2.VideoWriter_fourcc(*'DX50')

## 카메라 속성을 실행창에 출력
print('width x height: ',size)
print('VideoWriterfourcc: ', fourcc)
print(f'delay: {delay}')
print('fps: ',fps)

## 카메라 속성 지정
capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])


## 동영상파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter('D:/github/OpenCV-Python/2022-10-04/save_videos/test_video1.avi', fourcc, fps, size)

while True:
    ret, frame = capture.read()
    if cv2.waitKey(30) >= 0:
        break # 스페이스바로 종료

    writer.write(frame)
    
    title = 'Camera'
    cv2.imshow(title, frame)

writer.release()
capture.release()