n = int(input('Введите количество слов'))
a = 1
result = ''
while a <= n:
    x = input('Введите слово')
    result = str(result + ' ' + x)
    a = a + 1
print(result)