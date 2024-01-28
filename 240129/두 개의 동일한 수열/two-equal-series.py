# 변수 선언 및 입력:
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
A.sort()
B.sort()

for i in range(n):
    for j in range(n):
        if A[i] == B[j]:
            cnt += 1

if cnt == n:
    print("Yes")
else:
    print("No")