import numpy as np, cv2

m1 = np.full((3, 6), 10, np.uint8)
m2 = np.full((3, 6), 50, np.uint8)

m_mask = np.zeros(m1.shape, np.uint8) # 관심 영역 지정
m_mask[:,3:] = 1 # 관심 영역만 1로 변경

m_add1 = cv2.add(m1, m2)
m_add2 = cv2.add(m1, m2, mask=m_mask) # 관심 영역만 덧셈 수행

m_div1 = cv2.divide(m1, m2) # 그냥 연산해버리면 소수점이 나와서 값이 버려짐
m1 = m1.astype(np.float32) # 자료형을 float으로 바꿔주는데 방법1
m2 = np.float32(m2)        # 방법2가 있다.
m_div2 = cv2.divide(m1, m2)

titles = ['m1', 'm2', 'm_mask', 'm_add1', 'm_add2', 'm_div1', 'm_div2']
for title in titles:
    print(f'[{title}] = \n{eval(title)}\n')
    # eval은 문자열로 들어온 입력을 변수나 함수로 인식하여 실행할 수 있게 해줌
    # 굉장히 편리하지만, 나쁜 예시로, 아이디나 비밀번호를 입력받는 부분에서 eval과 비슷한 함수를 사용했다가
    # 해커가 취약점 발견하고 관리자계정으로 접속을 하여 데이터를 갈취해 간 사례가 적지않게 있었음.
