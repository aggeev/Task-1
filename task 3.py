print('тип результата выражения 15*3 ', type (15*3))
print('тип результата выражения 15/3 ', type (15/3))
print('тип результата выражения 15//3 ', type (15//3))
print('тип результата выражения 15**3 ', type (15**3))


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