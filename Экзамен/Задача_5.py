a = input('Введите сроку: ')
b = ''
for i in a:
    if i.isdigit():
        b += i
    elif b != '':
        print(b)
        b = ''
        print(b)
