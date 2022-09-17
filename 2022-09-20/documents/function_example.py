# 코드의 재사용 (구구단)
## solution1 (for)
for i in range(1, 10):
    print(f"{2} x {i} = {2*i}")
for i in range(1, 10):
    print(f"{3} x {i} = {2*i}")
# ...
for i in range(1, 10):
    print(f"{8} x {i} = {2*i}")
for i in range(1, 10):
    print(f"{9} x {i} = {2*i}")

## solution2 (function)
def gogodan(num):
    for i in range(1, 10):
        return f"{num} x {i} = {num*i}"

print(gogodan(2))
print(gogodan(3))
# ...
print(gogodan(8))
print(gogodan(9))