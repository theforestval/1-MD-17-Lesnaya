def first():
    numbers = [5,10,15,25,30]
    number = int(input('Введите число '))
    if number in numbers:
        print('Поздравляю, вы угадали, число ', number, 'входит в ', numbers)
    else:
        print('Извините, число, ', number, 'не входит в ', numbers)

def second():
    numbers1 = [2,5,0,3,2,0,1,8]
    numbers2 = []
    for item in numbers1:
        if item not in numbers2:
            numbers2.append(item)
    print(numbers2)

second()



def third():
    week = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница','суббота','воскресенье')
    a = int(input('Сколько выходных вы хотите? '))
    if a == 1:
        print('Ваши выходные дни: ', week[6])
        print('Ваши рабочие дни: ', week[0:6])
    if a == 2:
        print('Ваши выходные дни: ', week[5], week[6])
        print('Ваши рабочие дни: ', week[0:5])
    if a == 3:
        print('Ваши выходные дни: ', week[4:6], week[6])
        print('Ваши рабочие дни: ', week[0:4])
    if a == 4:
        print('Ваши выходные дни: ', week[3:6],week[6])
        print('Ваши рабочие дни: ', week[0:3])
    if a == 5:
        print('Ваши выходные дни: ', week[2:6], week[6])
        print('Ваши рабочие дни: ', week[0:2])
    if a == 6:
        print('Ваши выходные дни: ', week[1:6], week[6])
        print('Ваши рабочие дни: ', week[0])
    if a == 7:
        print('Ваши выходные дни: ', week)
        print('Ваши рабочие дни: нет')
    if a == 0:
        print('Ваши выходные дни: нет')
        print('Ваши рабочие дни: ', week)





