import random

print('Добро пожаловать в казино! Пожалуйста выберите значение от 1 до 10 и цвет поля')
print('1 - красный,2 - чёрный')
i = 1


while i <= 5:
    a = random.randint(1, 10)
    b = random.randint(1, 2)
    c = int(input('Введите значение от 1 до 10: '))
    l = int(input('Выберите цвет: '))

    if a == c and b == l:
        i = i + 1
        print('Вы выйграли!')
        break
    elif b == 1:
        i = i + 1
        print('Вы проиграли,компьютер загадал: ', a, 'chernoe')
    elif b == 2:
        i = i + 1
        print('Вы проиграли,компьютер загадал: ', a, 'krasnoe')
