import numpy as np

# example1
zeros = np.zeros((2, 5), np.int32)
ones = np.ones((3, 1), np.uint8)
emptys = np.empty((1, 5), np.float64)
fulls = np.full(5, 15, np.float32)

print(zeros)
print(ones)
print(emptys)
print(fulls)

# example2
np.random.seed(10)
a = np.random.rand(2, 3)
b = np.random.randint(1, 100, 6)
print(a)
print(b)
b = b.reshape(2,-1)
print(b)

# solution1
list1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
list2 = np.array([10, 20, 30, 40, 50, 60, 70, 80])

list1 = list1.reshape(2, -1)
list2 = list2.reshape(2, -1)

print(list1 + list2)
print(list1 * list2)

# solution2
np.random.seed(10)
np_a = np.random.rand(10)
sum_a = 0
for a in np_a:
    sum_a += a
print(np_a)
print(sum_a)
print(sum_a/10)

# solution3
np.random.seed(10)
np_a = np.random.rand(1, 10)
print(np_a)
print(np_a.sum())
print(np_a.mean())

# solution4
from collections import Counter
np.random.seed(10)
arr = np.random.randint(0, 50, 500)
more_data = Counter(arr).most_common()[0]
print(f'가장 많이 나온 원소: {more_data[0]}')
print(f'중복횟수: {more_data[1]}회')

# solution5 (for + dict)
np.random.seed(10)
result = {}
arr = np.random.randint(0, 50, 500)

# 딕셔너리에 중복값을 담는 과정
for a in arr:
    if a not in result:
        result[int(a)] = 1
    else:
        result[int(a)] += 1

# 중복이 가장 많은 값만 변수에 저장
max_key, max_value = 0, 0
for k, v in result.items():
    if v > max_value:
        max_value = v
        max_key = k    
print(f'가장 많이 나온 원소: {max_key}')
print(f'중복횟수: {max_value}회')

# solution6 (for + dict + lambda)
np.random.seed(10)
result = {}
arr = np.random.randint(0, 50, 500)

# 딕셔너리에 중복값을 담는 과정
for a in arr:
    if a not in result:
        result[a] = 1
    else:
        result[a] += 1

# 중복이 많은 횟수대로 정렬
result = sorted(result.items(), key=lambda x:x[1], reverse=True)

print(f'가장 많이 나온 원소: {result[0][0]}')
print(f'중복횟수: {result[0][1]}회')
