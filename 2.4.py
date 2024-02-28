print('Посчитайте сумму чисел 6 и 2')
a = 1
while a <= 3:
    sum = int(input('6 + 2 = '))
    a = a + 1
    if sum !=8:
        print('Ответ неверный')
    else:
        print('Правильно!')
        break
    if a==4:
        print('Попытки закончились')
