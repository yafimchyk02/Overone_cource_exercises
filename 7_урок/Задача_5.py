a = input('Введите символ 1: ')
b = input('Введите символ 2 : ')
c = int(input('Ширина: '))
l = int(input('Высота: '))
i = 0
print(c*a)
for i in range(1,l-1):
    print(a+(c-2)*b+a)
print(c*a)

