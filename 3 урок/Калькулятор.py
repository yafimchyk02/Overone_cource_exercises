a = float(input('Введите первое число'))
b = float(input('Введите второе число'))
c = str(input('Введите операцию: (+, -, /, *): '))

print('a = ',a)
print('b = ',b)


if c == '+':
    print('a + b = ', a + b)
elif c == '-':
    print('a - b =', a - b)
elif c == '/':
    print('a / b =', a / b)
elif c == '*':
    print('a * b =', a * b)

