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