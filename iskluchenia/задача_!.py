a = int(input('Введите число 1'))
b = int(input('Введите число 2'))

try:
    l = a / b
except ZeroDivisionError:
    print('Произошла ошибка при делении на 0')
else:
    print('ошибок нет, возвожу в квадрат', (a / b) ** 2)
finally:
    print('Операция выполнена!')
