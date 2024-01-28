n = int(input())
m =[]

while True:
    if n < 2:
        m.append(n)
        break

    m.append(n % 2)
    n //= 2

for i in m[::-1]:
    print(i, end = "")