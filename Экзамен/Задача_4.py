import random
b = int
s = str
k = int(input('Задайте количество введенных чисел: '))
isk = int(input('Задайте искомую цифру: '))
n = str(isk)
i = 0
while i < k:
    i += 1
    b = random.randint(1,99999)
    s = str(b)
    print('Рандомное число: ',b,'Искомая цифра встретилась: ',s.count(n),'раз')


    