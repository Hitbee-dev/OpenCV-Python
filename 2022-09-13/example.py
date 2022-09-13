# dict
data = {'Id': 'kimchan', 'Pw':'chan'}
print(data, type(data))
print(data['Id'])
print(data['Pw'])

# 삽입정렬1
tv = (8, 41, 21, 3, 35, 5, 25, 54)

arr = list(tv)
# 1~10까지 반복
for end in range(1, len(arr)):
    # 2~0까지 반복?
    print("====================")
    for i in range(end, 0, -1):
        # 이전 값이랑 현재 값이랑 비교
        if arr[i-1] > arr[i]:
            # 이전 값이 더 크다면 두 개의 값을 바꿈
            arr[i-1], arr[i] = arr[i], arr[i-1] 

print(arr)

# 삽입정렬2
tv = (8, 41, 21, 3, 35, 5, 25, 54)
lv = []
for i in range(len(tv)):
    pos = -1
    for j in range(len(lv)):
    # if tv[i] > lv[j]: # descending order, 내림차순
        if tv[i] <= lv[j]: # ascending order, 오름차순
            pos = j
            break
    if pos == -1: # len(lv) == 0, for loop j에서 pos을 못 찾았는 경우
        lv.append(tv[i])
    else:
        lv.insert(pos, tv[i])
print(tv)
print(lv)