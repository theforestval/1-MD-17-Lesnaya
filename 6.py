def firsta():
    dict = {'швеция': 'стокгольм', 'норвегия': 'осло', 'финляндия': 'хельсинки', 'великобритания': 'лондон', 'ирландия': 'дублин'}
    for key in dict:
        print(key, "-", dict[key])

def firstb():
    dict = {'швеция': 'стокгольм', 'норвегия': 'осло', 'финляндия': 'хельсинки', 'великобритания': 'лондон', 'ирландия': 'дублин'}
    st = str(input('Введите название страны: '))
    if st in dict:
        stt = dict.get(st)
        print(stt)
    else:
        print ("Страна не найдена")

def firstc():
    dict = {'швеция': 'стокгольм', 'норвегия': 'осло', 'финляндия': 'хельсинки', 'великобритания': 'лондон', 'ирландия': 'дублин'}
    sort_dict = sorted(dict.keys())
    for key in sort_dict:
        print(key, "-", dict[key])

def second():
    one = {'а','в','е', 'и','н','о','р','с','т'}
    two = {'д','к','л','м','п','у'}
    three = {'б','г','ё','ь','я'}
    four = {'й','ы'}
    five = {'ж','з','х','ц','ч'}
    eight = {'ш','э','ю'}
    ten = {'ф','щ','ъ'}
    sum = 0
    word = str(input('Введите слово: '))
    letters = list(word)
    for letter in letters:
        if letter in one:
            sum += 1
        if letter in two:
            sum += 2
        if letter in three:
            sum += 3
        if letter in four:
            sum += 4
        if letter in five:
            sum += 5
        if letter in eight:
            sum += 8
        if letter in ten:
            sum += 10
    print(sum)

second()


