p = 1
n = 0
c = []
while n < 10000:
    n = 2 ** (p - 1) * (2 ** p - 1)
    p = p + 1
    c.append(n)
print('Все совершенные числа от 1 до 10000: ',c)


