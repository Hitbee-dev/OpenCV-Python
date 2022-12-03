import numpy as np, cv2
import matplotlib.pyplot as plt

# 중복으로 사용되는 코드 재활용
def shift_info(img):
    dst = np.zeros(img.shape, img.dtype)
    h, w = dst.shape[:2]
    cx, cy = w//2, h//2
    
    # 영상의 크기가 짝수일 때는 괜찮은데, 홀수인 경우 왜곡이 발생
    # fftshift와 ifftshift로 구분 구현
    xo = 0 if w % 2 == 0 else 1
    ''' 위랑 같은 코드
    if w%2 == 0:
        xo = 0
    else:
        xo = 1
    '''
    yo = 0 if h % 2 == 0 else 1
    return cx, cy, xo, yo, dst

def fftshift(img):
    cx, cy, xo, yo, dst = shift_info(img)
    dst[cy:, cx:] = np.copy(img[0:cy+yo, 0:cx+xo])  # 1사분면 -> 3사분면
    dst[0:cy, 0:cx] = np.copy(img[cy+yo:, cx+xo:])  # 3사분면 -> 1사분면
    dst[0:cy, cx:] = np.copy(img[cy+yo:, 0:cx+xo])  # 2사분면 -> 4사분면
    dst[cy:, 0:cx] = np.copy(img[0:cy+yo, cx+xo:])  # 4사분면 -> 2사분면
    return dst

def ifftshift(img):
    cx, cy, xo, yo, dst = shift_info(img)
    dst[cy+yo:, cx+xo:] = np.copy(img[0:cy, 0:cx])  # 1사분면 -> 3사분면
    dst[0:cy+yo, 0:cx+xo] = np.copy(img[cy:, cx:])  # 3사분면 -> 1사분면
    dst[0:cy+yo, cx+xo:] = np.copy(img[cy:, 0:cx])  # 2사분면 -> 4사분면
    dst[cy+yo:, 0:cx+xo] = np.copy(img[0:cy, cx:])  # 4사분면 -> 2사분면
    return dst

def calc_spectrum(complex):
    # 만약 이미지가 2차원 행렬이라면
    if complex.ndim == 2:
        # 복소수 객체 행렬을 실수 행렬로 변환
        dst = abs(complex)
    # 만약 이미지가 3차원 행렬이라면
    else:
        dst = cv2.magnitude(complex[:,:,0], complex[:,:,1])
        '''
        1. 2D 벡터의 x 좌표를 나타내는 행렬
        2. 2D 벡터의 y 좌표를 나타내는 행렬
        -> 두 행렬의 크기는 같아야 하고, 타입은 실수형이어야 함
        '''
    dst = cv2.log(dst + 1)
    cv2.normalize(dst, dst, 0, 255, cv2.NORM_MINMAX)
    return cv2.convertScaleAbs(dst)

# 고속 푸리에 변환
def FFT(image):
    # 푸리에 변환
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    # 주파수 시프트
    dft = fftshift(dft)
    # 주파수 스펙트럼 영상
    spectrum = calc_spectrum(dft)
    return dft, spectrum

# 역 고속 푸리에 변환
def IFFT(dft, shape):
    # 주파수 영역에서 원래 영상으로 변환
    dft = ifftshift(dft)
    # 역 푸리에 변환 [:,:,0]은 실수부, [:,:,1]은 허수부
    img = cv2.idft(dft, flags=cv2.DFT_SCALE)[:,:,0]
    # 영삽입(zero-padding) 부분 제거
    img = img[:shape[0], :shape[1]]
    # 절대값 및 uint8 스케일링
    return cv2.convertScaleAbs(img)

# 이미지 읽기
image = cv2.imread("D:/github/OpenCV-Python/2022-12-06/images/12th_taegeuk_warrior.png", cv2.IMREAD_GRAYSCALE)

# 행렬 중심점 구하기
cy, cx = np.divmod(image.shape, 2)[0]

# FFT 수행 및 셔플링
dft, spectrum = FFT(image)

# 저주파 통과 필터
lowpass = np.zeros(dft.shape, np.float32)

# 고주파 통과 필터
highpass = np.ones(dft.shape, np.float32)

# 2개 채널로 값 지정
cv2.circle(lowpass, (cx, cy), 30, (1, 1), -1)
cv2.circle(highpass, (cx, cy), 30, (0, 0), -1)

# 주파수 필터링 = 주파수 계수 * 필터행렬
lowpassed_dft = dft * lowpass
highpassed_dft = dft * highpass

# 푸리에 역변환
lowpassed_img = IFFT(lowpassed_dft, image.shape)
highpassed_img = IFFT(highpassed_dft, image.shape)

# 반복문으로 이미지 한번에 출력
titles = ['image', 'lowpassed_img', 'highpassed_img', 'spectrum', 'lowpassed_dft', 'highpassed_dft']
plt.figure(figsize=(12, 6))
for idx, title in enumerate(titles):
    plt.subplot(2, 3, idx+1)
    plt.axis("off")
    plt.title(title)
    if idx < 4:
        plt.imshow(eval(title), cmap='gray')
    else:
        plt.imshow(calc_spectrum(eval(title)), cmap='gray')
plt.show()