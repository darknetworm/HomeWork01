startKm = float(input('Введите начальную дистанцию спортсмена: '))
finishKm = float(input('Введите необходимую дистанцию: '))
day = 1

if finishKm <= startKm:
    print('Спортсмен уже пробегает {} км'.format(startKm))

else:
    while startKm < finishKm:
        startKm = startKm + (startKm * 0.1)
        day += 1

print('На {} день спортсмен пробежит не менее {} километров'.format(day, finishKm))
