a, b = map(int, input().split())
n = int(input())

res=0
for i in range(len(n)):
    res += (a**i) * int(n[i])
new_num=res

res=""
while True:
    if new_num<b:
        res = str(new_num) + res
        break
    else:
        res = str(new_num%b) + res
        new_num//=2
print(res)