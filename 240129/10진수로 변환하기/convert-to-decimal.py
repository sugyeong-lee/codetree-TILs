n = list(map(int, list(input())))
num = 0
k = len(n)

for i in range(k):
    num = num * 2 + n[i]

print(num)


# 입력관련 생각해보기 list, split