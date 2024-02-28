result = ''
x = ''
while x!= 'стоп':
    x = input('Введите слово')
    if x == 'стоп':
        break
    result = str(result + ' ' + x)
print(result)