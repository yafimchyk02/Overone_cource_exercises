x = ('привет','пока', 'да','нет')
y = [1,2,3,'a','b','c','abc',4,5,6]
print(x,y)
def func(f):
    dlina_x = 0
    chisla_y = 0
    bukvi_y = 0

    x = ('привет','пока', 'да','нет')
    y = [1,2,3,'a','b','c','abc',4,5,6]
    c = str(y)

    if f == 'кортеж':
        for i in x:
            dlina_x += len(i)
        print('длина всех слов кортежа:', dlina_x)
    if f == 'список':
        for l in c:
            if l.isalpha():
                bukvi_y += 1
            elif l.isdigit():
                chisla_y += 1
        print('кол-во чисел: ', chisla_y)
        print('кол-во букв: ',bukvi_y)


print(func(input('Что обработает функция (кортеж или список)? : ')))