import numpy as np

m1 = np.random.rand(3, 5) # 3 * 5 행렬 랜덤으로 생성
print(m1)

m2 = m1.copy() * 1000//10 # *1000하고, 10으로 나눈 몫을 취하면 0~100의 난수 생성
print(m2)
