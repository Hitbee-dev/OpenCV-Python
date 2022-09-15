names = ["홍길동", "이순신", "세종", "아이언맨", "슈퍼맨"]
scores = [30, 50, 100, 20, 70]

# solution1 (range)
results = {}
for i in range(5):
    results[names[i]] = scores[i]
print(results)

# solution2 (for each)
results = {}
for name in names:
    results[name] = scores[names.index(name)]
print(results)

# solution3 (enumerate)
results = {}
for idx, name in enumerate(names):
    results[name] = scores[idx]
print(results)

# solution4 (zip)
results = {}
for name, score in zip(names, scores):
    results[name] = score
print(results)