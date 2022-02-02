import random
a = random.randint(100,999)
b = str(a)
print(b)
print(b[0], b[1], b[2] )
c = int(b[0])
v = int(b[1])
n = int(b[2])
print('Сумма цифр: ', c + v + n)
