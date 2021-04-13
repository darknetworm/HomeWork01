num = input('Введите целое положительное число: ')

countNum = len(num)
maxNum = int(num[0])
i = 1

while i < countNum:
    if maxNum < int(num[i]):
        maxNum = int(num[i])
    i += 1

print('Максимальная цифра в числе: ', maxNum)