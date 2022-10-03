import cv2

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    if cv2.waitKey(30) >= 0:
        break # 스페이스바로 종료

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE) # 노출 속성
    title = 'Camera'
    cv2.imshow(title, frame)
capture.release()