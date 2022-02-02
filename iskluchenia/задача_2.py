a = int(input('Введите число 1'))
b = int(input('Введите число 2'))
try:
    l = a / b
    print('Результат преобразования',l)
except ValueError:
    print('Преобразование прошло  неотлично')
except ZeroDivisionError:
    print('Произошла ошибка при делении на 0')
except Exception:
    print('Общее исключение')
finally:
    print('Операция выполнена!')
