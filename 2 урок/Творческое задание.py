print('Добро пожаловать в игру "Кто хочет стать миллионером".')
print('В данной игре вам предстоит ответить на 3 вопроса чтобы выйграть 1 миллион долларов!')
print('И только сегодня вы получаете уникальную возможность отвечать на все вопросы неограниченное количество раз!')
print('Кроме последнего вопроса!')

while True:
    print('Первый вопрос')  # Первый вопрос
    a = str('Как звали Гитлера?')
    print(a)
    d = str('Адольф')
    g = str('Густаво')
    j = str('Леонардо')
    print('1.', d, '2.', g, '3.', j)
    b = int(input('Ваш ответ:'))
    if b == 2 or b == 3:
        print('Ответ неверный, начните заново')
    else:
        break

print('Поздавляем, вы выйграли 200 000 USD!')

while True:
    print('Второй впрос')  # Второй вопрос
    n = str('В каком году отмненили крепостное право?')
    print(n)
    q = int(1861)
    w = int(1456)
    e = int(1893)
    print('1.', w, '2.', q, '3.', e)
    k = int(input('Ваш ответ:'))
    if k == 1 or k == 3:
        print('Ответ неверный,начните заново')
    else:
        break
print('Поздравляем, вы выйграли 600 000 USD! ')

print('Третий вопрос')  # Третий вопрос
l = str('Как звали создателя автомобильной марки Ferrari?')
print(l)
z = str('Энцо')
x = str('Джовани')
c = str('Федерико')
print('1.', c, '2.', x, '3.', z)
p = int(input('Ваш ответ:'))
if p == 3:
    print('Ответ верный,вы выйграли 1 000 000 USD')
elif p == 1 or p == 2:
    print('Ответ неверный, но вы почти выйграли,попробуйте ещё раз!')
    l = str('Как звали создателя автомобильной марки Ferrari?')
    print(l)
    z = str('Энцо')
    x = str('Джовани')
    c = str('Федерико')
    print('1.', c, '2.', x, '3.', z)
    p = int(input('Ваш ответ:'))
    if p == 3:
        print('Ответ верный,вы выйграли 1 000 000 USD')
    else:
        print('Ответ неверный, игра окончена')
