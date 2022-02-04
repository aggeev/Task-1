a = list(range(1 , 1001, 2))
for i in range(1, len(a)):
    a[i] = a[i] ** 3
summ = 0
summ_all = 0
for number in a:
    num = number
    while num > 0:
        summ += num % 10
        num = num // 10
    if summ % 7 == 0:
        summ_all += number
    summ = 0
print(summ_all)
summ_all = 0
for i in range(1, len(a)):
    a[i] = a[i] + 17
for number in a:
    num = number
    while num > 0:
        summ += num % 10
        num = num // 10
    if summ % 7 == 0:
        summ_all += number
    summ = 0
print(summ_all)