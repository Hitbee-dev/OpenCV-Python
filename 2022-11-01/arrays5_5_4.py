import numpy as np, cv2
src1 = np.array([1, 2, 3, 1, 2, 3], np.float32).reshape(2, 3)
src2 = np.array([1, 2, 3, 4, 5, 6], np.float32).reshape(2, 3)
src3 = np.array([1, 2, 1, 2, 1, 2], np.float32).reshape(3, 2)
alpha, beta = 1.0, 1.0

print(src1)
print(src2)
print(src3)

dst1 = cv2.gemm(src1, src2, alpha, None, beta, flags = cv2.GEMM_1_T)
print(dst1)

dst2 = cv2.gemm(src1, src2, alpha, None, beta, flags = cv2.GEMM_2_T)
print(dst2)

dst3 = cv2.gemm(src1, src3, alpha, None, beta)
print(dst3)

