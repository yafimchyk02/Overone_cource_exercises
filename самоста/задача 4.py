while True:
    a = int(input('Введите число 1: '))
    b = int(input('Введите число 2: '))
    try:
        l = a / b
    except ZeroDivisionError:
        print('Произошла ошибка при делении на 0')
        break
    else:
        print('Всё впорядке, а теперь попробуйте поделить на ноль')
    finally:
        print('Операция выполнена!')