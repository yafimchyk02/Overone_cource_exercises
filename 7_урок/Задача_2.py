a = int(input('Введите первое число a: '))
b = int(input('Введите второе число b: '))
c = int(input('Введите третье число c: '))
if a > b and a < c or a > c and a < b:
    print('a среднее')
elif b > a and b < c or b > c and b < a:
    print('b среднее')
elif c > a and c < b or c > b and c < a:
    print('c среднее')
