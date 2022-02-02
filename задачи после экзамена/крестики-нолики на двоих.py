a = ['*', '*', '*']  # по горизонтали поле № 1
b = ['*', '*', '*']  # по горизонтали поле № 2
c = ['*', '*', '*']  # по горизонтали поле № 3
q = ['1', '2', '3']
l = ['x', 'o']
vtoroi = str

print('  ', ' '.join(q))
print('a:', ' '.join(a))
print('b:', ' '.join(b))
print('c:', ' '.join(c))

print('''Добро пожаловать в игру крестики-нолики! Место куда будет вставлен ваш элемент определяетсяпо следующим правилам:
позиция по горизонтали соответсвенно (a,b,c)
позиция по вертикали сооответсвенно (1,2,3 и т.д.)
значения ('0' или 'x' вставляются игроками по очереди
размер поля 3 x 3''')

viborka_pervogo = input('Игрок 1 выберите крестик или нолик (x или o):')
if viborka_pervogo == 'x':
    vtoroi = 'o'
elif viborka_pervogo == 'o':
    vtoroi = 'x'

i = 0

while i < 9:
    i += 1
    h = 0
    j = 0
    k = 0
    if i % 2 != 0:
        print('Игрок 1 ходит')
        position = input('Выберите позицию по горизонтали: ')
        pos_vert = int(input('Выберите позицию по вертикали: '))
        for h in a:
            for j in b:
                for k in c:
                    if a[pos_vert - 1] == 'x' or a[pos_vert - 1] == 'o' or b[pos_vert - 1] == 'x' or b[
                        pos_vert - 1] == 'o' or c[pos_vert - 1] == 'x' or c[pos_vert -1] == 'o':
                        print('Эта позиция занята, выбирете другую')
                        position = input('Выберите позицию по горизонтали: ')
                        pos_vert = int(input('Выберите позицию по вертикали: '))
        if position == 'a':
            a[pos_vert - 1] = viborka_pervogo
        elif position == 'b':
            b[pos_vert - 1] = viborka_pervogo
        elif position == 'c':
            c[pos_vert - 1] = viborka_pervogo
        print('игрок 1 сделал свой выбор: ')
        print('  ', ' '.join(q))
        print('a:', ' '.join(a))
        print('b:', ' '.join(b))
        print('c:', ' '.join(c))

    else:
        print('Игрок 2 ходит')
        position = input('Выберите позицию по горизонтали: ')
        pos_vert = int(input('Выберите позицию по вертикали: '))
        for h in a:
            for j in b:
                for k in c:
                    if a[pos_vert - 1] == 'x' or a[pos_vert - 1] == 'o' or b[pos_vert - 1] == 'x' or b[
                        pos_vert - 1] == 'o' or c[pos_vert - 1] == 'x' or c[pos_vert -1] == 'o':
                        print('Эта позиция занята, выбирете другую')
                        position = input('Выберите позицию по горизонтали: ')
                        pos_vert = int(input('Выберите позицию по вертикали: '))
        if position == 'a':
            a[pos_vert - 1] = vtoroi
        elif position == 'b':
            b[pos_vert - 1] = vtoroi
        elif position == 'c':
            c[pos_vert - 1] = vtoroi
        print('игрок 2 сделал свой выбор: ')
        print('  ', ' '.join(q))
        print('a:', ' '.join(a))
        print('b:', ' '.join(b))
        print('c:', ' '.join(c))
    if a[0] == a[1] == a[2] == 'x' or a[2] == b[2] == c[2] == 'x' or c[0] == c[1] == c[2] == 'x' or a[0] == b[0] == c[
        0] == 'x' or a[0] == b[1] == c[2] == 'x' or a[2] == b[1] == c[0] == 'x':
        if viborka_pervogo == 'x':
            print('Первый игрок выйграл!')
        elif viborka_pervogo == 'o':
            print('Второй игрок выйграл!')
        break
    elif a[0] == a[1] == a[2] == 'o' or a[2] == b[2] == c[2] == 'o' or c[0] == c[1] == c[2] == 'o' or a[0] == b[0] == c[
        0] == 'o' or a[0] == b[1] == c[2] == 'o' or a[2] == b[1] == c[0] == 'o':
        if viborka_pervogo == 'o':
            print('Первый игрок выйграл!')
        elif viborka_pervogo == 'x':
            print('Второй игрок выйграл!')
        break
