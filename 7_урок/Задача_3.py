import random
a = random.randint(0,1000)
b = random.randint(0,1000)
print(a)
print(b)
if a % 2 != 0:
    print('Первое нечётное')
elif b % 2 != 0:
    print('Второе нечётное')
else:
    print('Оба чётные')
