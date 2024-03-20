a = int(input('Введите число '))

def f():
    if a%7==0:
        print('Число делится на семь', a)
    else:
        print('Число не делится на семь', a)

def s():
    try:
        a = int(input('Введите число '))
        b = a//200
        return b
    except (ValueError, ZeroDivisionError):
        print('Ошибка')

def t():
    



