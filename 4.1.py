
def f():
    a = int(input('Введите число '))
    if a%7==0:
        print('Число делится на семь', a)
    else:
        print('Число не делится на семь', a)


def s():
    a = int(input('Введите число '))
    try:
        a = int(input('Введите число '))
        b = a//200
        return b
    except (ValueError, ZeroDivisionError):
        print('Ошибка')


def t():
    a = str(input('Введите дату '))
    b = a.split('.')
    if int(b[0])*int(b[1])==int(b[2]):
        print('Число магическое')
        return False
    else:
        print('Число немагическое')
        return True

t()






    



