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



duration = int(input("введите количество секунд"))
if duration < 60:
    print(str(duration) + ' сек')
elif duration < 3600:
    print(str(duration // 60) + ' мин ' + str(duration % 60) + ' сек')
elif duration < 3600 * 24:
    print(duration // 3600, 'hr', duration % 3600 // 60, 'min', duration % 60, 'sec')
else:
    days = duration // (3600 * 24)
    hours = duration % (3600 * 24) // 3600
    mins = duration % 3600 // 60
    sec = duration % 60
    print(days, 'days', hours, 'hr', mins, 'min', sec, 'sec')