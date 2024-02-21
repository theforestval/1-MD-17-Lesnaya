colour1 = input("Введите первый цвет")
if colour1 == "синий" or colour1 == "красный" or colour1 == "желтый":
    colour2 = input("Введите второй цвет")
else:
    print("Ошибка")
if colour1 == "красный" and colour2 == "синий" or colour1 == "синий" and colour2 == "красный":
    print("фиолетовый")
if colour1 == "красный" and colour2 == "желтый" or colour1 == "желтый" and colour2 == "красный":
    print('оранжевый')
if colour1 == "синий" and colour2 == "желтый" or colour1 == "желтый" and colour2 == "синий":
    print('зеленый')
