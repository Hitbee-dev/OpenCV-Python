# 변수
X = 30
print(f'X: {X}', type(X))
Y = "30"
print(f'Y: {Y}', type(Y))

# int와 str의 연산 차이
X = 30 + 30
print(f'X: {X}', type(X))
Y = "30" + "30"
print(f'Y: {Y}', type(Y))

# list
list_data = ['a', 'b', 'c', 'd']
print(list_data, type(list_data))

# tuple
tuple_data = ('a', 'b', 'c', 'd')
print(tuple_data, type(tuple_data))

# set은 중복 불가능한 배열이며, 순서를 보장받을 수 없음
set_data = set(['a', 'b', 'c', 'd'])
print(set_data, type(set_data))

# dict
dict_data = {'a':1, 'b':2, 'c':3, 'd':4}
print(dict_data, type(dict_data))

# List 슬라이스 연산
list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_data)
print(list_data[:])
print(list_data[:2])
print(list_data[::2])
print(list_data[::-1])

# pythonic한 if문
list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(list_data)):
    if list_data[i] is 4:
        print(list_data[i])

# range
list_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(7):
    print(list_data[i])

# for each
list_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in list_data:
    print(i)

# enumerate
list_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for idx, data in enumerate(list_data):
    print(idx, data)

# function
list_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def sum_data(data):
    return data + 1

for data in list_data:
    print(sum_data(data))

list_data2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]

for data in list_data2:
    print(sum_data(data))