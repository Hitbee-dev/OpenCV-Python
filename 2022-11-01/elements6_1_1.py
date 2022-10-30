import numpy as np

def mat_access1(mat): # 직접 접근 방법
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i, j]
            mat[i, j] = k * 2

def mat_access2(mat): # item, itemset 방법
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat.item(i, j)
            mat.itemset((i, j), k * 2)

mat1 = np.arange(10).reshape(2, 5)
mat2 = np.arange(10).reshape(2, 5)

print(f"원소 처리 전: \n{mat1}\n")
mat_access1(mat1)
print(f"원소 처리 후: \n{mat1}\n")

print(f"원소 처리 전: \n{mat2}\n")
mat_access2(mat2)
print(f"원소 처리 후: \n{mat2}\n")