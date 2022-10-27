import numpy as np, cv2

m1 = np.random.rand(3, 5) # 3 * 5 행렬 랜덤으로 생성
m2 = m1.copy() * 1000//10 # *1000하고, 10으로 나눈 몫을 취하면 0~100의 난수 생성

reduce_sum = cv2.reduce(m2, dim=0, rtype=cv2.REDUCE_SUM)
reduce_avg = cv2.reduce(m2, dim=1, rtype=cv2.REDUCE_AVG)
reduce_max = cv2.reduce(m2, dim=0, rtype=cv2.REDUCE_MAX)
reduce_min = cv2.reduce(m2, dim=1, rtype=cv2.REDUCE_MIN)

print(f"[m2] = \n {m2} \n")
print(f"[sum] = {reduce_sum.flatten()}")
print(f"[avg] = {reduce_avg.flatten()}")
print(f"[max] = {reduce_max.flatten()}")
print(f"[min] = {reduce_min.flatten()}")