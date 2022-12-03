'''
1. select rect창에 원본 이미지 띄우기
2. select rect창에 드래그 할 수 있는 4좌표 생성
3. 드래그 할 수 있는 4개의 좌표를 서로 선으로 이어줌
4. 드래그 했을 때 투영된 이미지 sub window에 실시간으로 출력
'''

import numpy as np, cv2

# 생성된 네모 박스를 잡아 끌수 있도록 기능 모듈화
def contain(p, p1, p2):
    # x, y의 위치가 네모박스 안에 있는지 비교문 사용
    return p1[0] <= p[0] < p2[0] and p1[1] <= p[1] < p2[1]

# 원본 이미지를 그리기 위한 함수
def draw_rect(img):
    # 1줄 for문
    rois = [(p - small, small * 2) for p in pts1]

    ''' 위 코드랑 같은 기능을 함
    rois = []
    for p in pts1:
        rois.append((p-small, small * 2))
    '''

    # 현재 네모 박스들의 위치 반복, np.int32를 준 이유는 좌표 값은 소수점이면 안되기 때문
    for (x, y), (w, h) in np.int32(rois):
        ''' 수업에 필요 없는 내용이라 제거
        # 관심 영역 지정, 각 네모 박스들의 위치를 변경
        roi = img[y:y+h, x:x+w]
        # 각 네모 박스 내부 투명도 변경, 0 ~ 255면 되기 때문에 8비트 unsigned int로 선언
        val = np.full(roi.shape, 80, np.uint8)
        # 이미지 합성
        cv2.add(roi, val, roi)
        '''
        # 현재 좌표에 맞춰 네모 그리기
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    # 각 네모 박스의 좌표를 선으로 이어줌
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)
    # 이미지 출력
    cv2.imshow("select rect", img)

def warp(img):
    # 이동 전 좌표, 이동 후 좌표를 주면 투시 변환 행렬을 반환하는 함수
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    # 반환될 이미지
    dst = cv2.warpPerspective(img, perspect_mat, (400, 350), cv2.INTER_CUBIC)
    '''
    1. 입력 영상
    2. 투시 변환 행렬
    3. 결과 영상 크기
    4. 보간법(4x4 이웃 픽셀을 참조)
        양선형 보간법인 cv2.INTER_LINEAR는 4개의 픽셀(2x2 이웃 픽셀)을 참조하기 때문에 속도도 빠르고, 퀄리티도 적당하나,
        3차 회선 보간법인 cv2.INTER_CUBIC은 16개의 픽셀(4x4 이웃 픽셀)을 참조하기 때문에 속도는 느리나, 퀄리티가 좋다.
        Lanczos 보간법인 cv2.INTER_LANCZOS4는 64개의 픽셀(8x8 이웃 픽셀)을 참조하기 때문에 오래 걸리나, 퀄리티가 더 좋다.
        이거 말고도 더 있지만, 메인이 아니기 때문에 왜 사용하는지 간단하게만 설명
    '''
    # 이미지 출력
    cv2.imshow("perspective transform", dst)

def onMouse(event, x, y, flags, param):
    global check

    # 만약 마우스 왼쪽 버튼을 눌렀다면
    if event == cv2.EVENT_LBUTTONDOWN:
        '''
        박스의 현재 좌표
        1   2
        4   3
        '''
        for i, p in enumerate(pts1):
            # 마우스를 클릭했을때 박스 안의 범위를 적용시켜서 현재위치 반환
            p1, p2 = p - small, p + small
            # 만약 현재 마우스 위치가 박스의 위치랑 같다면
            if contain((x,y), p1, p2):
                # Mouse Drag Event를 구현하기 위해 전역변수인 check를 몇번째 박스인지 값을 바꿔줌
                check = i
    
    # 마우스에서 손 떼면 더이상 박스 안따라다니게 변경
    if event == cv2.EVENT_LBUTTONUP:
        check = -1
    
    # Mouse Event에 Drag 이벤트는 지원하지 않으니, 이렇게 구현하는 것
    if check >= 0:
        # 클릭한 박스를 움직이기 위해 해당 좌표만 변경
        pts1[check] = (x, y)
        # 클릭한 박스를 현재 위치에 맞게 그리기 위해 생성
        draw_rect(np.copy(image))
        # 현재 박스(범위)에 따라 투영된 이미지를 출력
        warp(np.copy(image))

image = cv2.imread("D:/github/OpenCV-Python/2022-12-06/images/perseptive.jpg")
# 핸드폰으로 찍은 이미지인데, 너무 길어서 반토막 냄
image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))

# 각 네모 박스의 크기 선언
small = np.array([12, 12])

# 마우스를 클릭했는지 안했는지 검사하기 위한 변수
check = -1

# 각 네모 박스의 위치 초기 선언
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)])

# 투영된 이미지를 출력하는 Window의 크기 선언
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])

# 원본 이미지를 띄우기 위함
draw_rect(np.copy(image))

# 원본 이미지가 띄워져 있는 Windows에 마우스 콜백함수 적용
cv2.setMouseCallback("select rect", onMouse, 0)
''' param에 0을 주는 이유
이런 이미지 실습의 경우 이미지를 param에 넣어 콜백함수에 같이 보내기도 하는데,
이번 실습은 좌표 값으로 이미지를 투영하기 때문에 굳이 이미지를 보낼 필요는 없다.
cv2.setMouseCallback("select rect", onMouse, image)
'''

# 키 입력 대기
cv2.waitKey(0)