income = int(input('Введите выручку фирмы: '))
outcome = int(input('Введите издержки фирмы: '))

if outcome > income:
    print('Фирма работает в убыток')
elif outcome == income:
    print('Фирма не приносит ничего')
else:
    print('Фирма приносит прибыль с рентабельностью: ', income / outcome)
    personal = int(input('Введите численность сотрудников фирмы: '))
    print('Прибыль фирмы в расчете на одного сотрудника составляет: ', income/personal)
    
