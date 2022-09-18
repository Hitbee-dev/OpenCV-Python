a = [10, 20, 30]

# solutuon1 (%)
print("배열에 있는 값은: %d %d %d 입니다." % (a[0], a[1], a[2]))

# solution2 (.format)
print("배열에 있는 값은: {} {} {} 입니다.".format(a[0], a[1], a[2]))

# solution3 (f-string)
print(f"배열에 있는 값은: {a[0]} {a[1]} {a[2]} 입니다.")