n = int(input('Введите 7-ми значное число: '))
d = str(n)
a = []
for i in d:
    i = int(i)
    a.append(i)
print(a)
b =[]
c =[]
suma = 0
pr = 1
for i in a:
    if i % 2 == 0:
        b.append(i)
    elif i % 2 != 0:
        c.append(i)
for i in a:
        if len(b) > len(c):
            suma = suma + i
if suma > 0:
    print('Сумма всех элементов: ', suma)


for i in a:
    if len(b) < len(c):
        pr = a[0] * a[2] * a[5]
if pr > 1:
    print('Произведение 1,3 и 6: ', pr)
