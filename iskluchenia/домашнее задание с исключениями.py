while True:
    c = []
    perv = int
    vtor = int
    dlina_str = int(input('Какую длину строки вы желаете сгенерировать? Введите: '))
    i = 0
    while i < dlina_str:
        c.append(input('Введиет число или слово: '))
        i += 1
    print(c)
    if ''.join(c).isdigit():
        try:
            perv = int(c[0])
            vtor = int(c[1])
            delenie = perv / vtor
            print('Результат деления первого числа на второе: ', delenie)
        except ZeroDivisionError:
            print('Возникла ошибка при делении на 0')
            print('Введите другие значения, пожалуйста')
        except ValueError:
            print('Нельзя делить буквы на цифры и наоборот')
    else:
        print('Требуется, чтобы строка состояла только из чисел! Повторите попытку')
