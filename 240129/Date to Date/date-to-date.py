m1, d1, m2, d2 = map(int, input().split())

num_day = [0, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
month, day = m1, d1
elapsed_days = 0


while True:

    elapsed_days += 1
    day += 1

    if day == num_day[month]:
        month += 1
        day = 1

    if month == m2 and day == d2:
        break
        
print(elapsed_days)