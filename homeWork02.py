inputTime = int(input('Введите время в секундах: '))

hours = inputTime // 3600
minutes = (inputTime - hours * 3600) // 60
seconds = inputTime - hours * 3600 - minutes * 60
print('Это будет (чч:мм:сс):')
print('{}:{}:{}'.format(hours, minutes, seconds))