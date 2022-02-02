import random

a = ['*', '*', '*']  # по горизонтали поле № 1
b = ['*', '*', '*']  # по горизонтали поле № 2
c = ['*', '*', '*']  # по горизонтали поле № 3
q = ['1', '2', '3']
l = ['x', 'o']
computer = str

print('  ', ' '.join(q))
print('a:', ' '.join(a))
print('b:', ' '.join(b))
print('c:', ' '.join(c))

print('''Добро пожаловать в игру крестики-нолики! Место куда будет вставлен ваш элемент определяетсяпо следующим правилам:
позиция по горизонтали соответсвенно (a,b,c)
позиция по вертикали сооответсвенно (1,2,3 и т.д.)
значения ('0' или 'x' вставляются игроками по очереди
размер поля 3 x 3''')

viborka_igroka = input('Игрок  выберите крестик или нолик (x или o): ')
if viborka_igroka == 'x':
    computer = 'o'
elif viborka_igroka == 'o':
    computer = 'x'

i = 0

while i < 9:
    i += 1
    h = 0
    j = 0
    k = 0
    if i % 2 != 0:
        print('Игрок ходит')
        position = input('Выберите позицию по горизонтали: ')
        pos_vert = int(input('Выберите позицию по вертикали: '))
        t = 0
        y = 0
        u = 0
        for t in a:
            for y in b:
                for u in c:
                    if a[pos_vert - 1] == 'x' or a[pos_vert - 1] == 'o' or b[pos_vert - 1] == 'x' or b[
                        pos_vert - 1] == 'o' or c[pos_vert - 1] == 'x' or c[pos_vert - 1] == 'o':
                        print('Эта позиция занята, выбирете другую')
                        position = input('Выберите позицию по горизонтали: ')
                        pos_vert = int(input('Выберите позицию по вертикали: '))
        if position == 'a':
            a[pos_vert - 1] = viborka_igroka
        elif position == 'b':
            b[pos_vert - 1] = viborka_igroka
        elif position == 'c':
            c[pos_vert - 1] = viborka_igroka
        print('игрок  сделал свой выбор: ')
        print('  ', ' '.join(q))
        print('a:', ' '.join(a))
        print('b:', ' '.join(b))
        print('c:', ' '.join(c))

    else:
        position = random.choice(['a','b','c'])
        pos_vert = random.randint(1,3)
        for h in a:
            for j in b:
                for k in c:
                    if a[pos_vert - 1] == 'x' or a[pos_vert - 1] == 'o' or b[pos_vert - 1] == 'x' or b[
                        pos_vert - 1] == 'o' or c[pos_vert - 1] == 'x' or c[pos_vert - 1] == 'o':
                        position = random.choice(['a', 'b', 'c'])
                        pos_vert = random.randint(1, 3)
        if position == 'a':
            a[pos_vert - 1] = computer
        elif position == 'b':
            b[pos_vert - 1] = computer
        elif position == 'c':
            c[pos_vert - 1] = computer
        print('компютер сделал свой выбор: ')
        print('  ', ' '.join(q))
        print('a:', ' '.join(a))
        print('b:', ' '.join(b))
        print('c:', ' '.join(c))
    if a[0] == a[1] == a[2] == 'x' or a[2] == b[2] == c[2] == 'x' or c[0] == c[1] == c[2] == 'x' or a[0] == b[0] == c[
        0] == 'x' or a[0] == b[1] == c[2] == 'x' or a[2] == b[1] == c[0] == 'x':
        if viborka_igroka == 'x':
            print('Игрок выйграл!')
        elif viborka_igroka == 'o':
            print('Компьютер выйграл!')
        break
    elif a[0] == a[1] == a[2] == 'o' or a[2] == b[2] == c[2] == 'o' or c[0] == c[1] == c[2] == 'o' or a[0] == b[0] == c[
        0] == 'o' or a[0] == b[1] == c[2] == 'o' or a[2] == b[1] == c[0] == 'o':
        if viborka_igroka == 'o':
            print('Игрок выйграл!')
        elif viborka_igroka == 'x':
            print('Компютер выйграл!')
        break
