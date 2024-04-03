def z1():
    import random
    a=[]
    for i in range(5):
        a.append(random.randint(1,50))
    b=input("напиши число от 1 до 50")
    if b in a:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
def z2():
    import random
    a=[]
    c=[]
    for i in range(50):
        a.append(random.randint(1,15))
        for i in range(len(a)-1):
            if a.count(a[i]) > 1:
                if a[i] in c:
                    continue
                else:
                    c.append(a[i])
    print(c)
def z3():
    d=("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    a=input("напишите сколько выходных вы хотите на неделе")
    



