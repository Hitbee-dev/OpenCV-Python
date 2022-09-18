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
np.random.seed(10)
np_a = np.random.rand(10)
sum_a = 0
for a in np_a:
    sum_a += a
print(np_a)
print(sum_a)
print(sum_a/10)

# solution2
np.random.seed(10)
np_a = np.random.rand(1, 10)
print(np_a)
print(np_a.sum())
print(np_a.mean())

# solution3
from collections import Counter
np.random.seed(10)
arr = np.random.randint(0, 50, 500)
more_data = Counter(arr).most_common()[0]
print(f'가장 많이 나온 원소: {more_data[0]}')
print(f'중복횟수: {more_data[1]}회')