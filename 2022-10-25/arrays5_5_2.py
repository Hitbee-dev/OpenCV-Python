import numpy as np, cv2

data = np.random.randint(0, 100, 15).reshape(3, 5)
print(data)
print("=======================")

sort1 = cv2.sort(data, cv2.SORT_EVERY_ROW)
sort2 = cv2.sort(data, cv2.SORT_EVERY_COLUMN)
sort3 = cv2.sort(data, cv2.SORT_EVERY_ROW+cv2.SORT_DESCENDING)
sort4 = np.sort(data, axis=1)
sort5 = np.sort(data, axis=0)
sort6 = np.sort(data, axis=1)[:, ::-1]

titles = ['sort1','sort2','sort3','sort4','sort5','sort6']
for title in titles:
    print(title)
    print(eval(title))