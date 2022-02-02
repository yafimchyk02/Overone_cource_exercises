import random

c = int
l = int
r = 0
o = 0 # Число из 4-ой итерации
p = 0 # Число из 4-ой итерации
j = ''
i = 0
while i < 7:
    a = int(input('Введите первое число от 1 до 20: '))
    b = int(input('Введите второе число от 1 до 20: '))
    print('Ваша пара:', '(', a, ',', b, ')')
    c = random.randint(1, 20)
    l = random.randint(1, 20)
    i += 1
    if i == 4:
        o = c
        p = l
    if a + b > c + l:
        r = r + 1
    elif a + b == c + l:
        j ='Есть случай равенства,числа из 4-ой итерации:'
print('Ваша пара оказалась больше',r,'раз!')
if len(j) > 1:
    print(j,'(',o,',',p,')')

