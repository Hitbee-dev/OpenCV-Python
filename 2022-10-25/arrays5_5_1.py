import numpy as np, cv2

def data_reduce(func, dim):
    global data
    print("==========================")
    print(f'{data}\n')
    return print(cv2.reduce(data, rtype=func, dim=dim))

data = np.random.randint(0, 20, size=(3, 5))
data = data.astype(np.float32)

data_reduce(cv2.REDUCE_AVG, 0)
data_reduce(cv2.REDUCE_AVG, 1)
data_reduce(cv2.REDUCE_SUM, 0)
data_reduce(cv2.REDUCE_SUM, 1)
data_reduce(cv2.REDUCE_MAX, 0)
data_reduce(cv2.REDUCE_MAX, 1)
data_reduce(cv2.REDUCE_MIN, 0)
data_reduce(cv2.REDUCE_MIN, 1)