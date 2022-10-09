import cv2

capture = cv2.VideoCapture('D:/github/OpenCV-Python/2022-10-04/save_videos/test_video1.avi')

fps = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)
fps_cnt = 0 # 현재 프레임 번호

while True:
    ret, frame = capture.read()
    if cv2.waitKey(30) >= 0:
        break # 스페이스바로 종료

    fps_cnt += 1
    print(fps_cnt)
    
    title = 'Camera'
    cv2.imshow(title, frame)

capture.release()