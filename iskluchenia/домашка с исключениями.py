while True:
    c = []
    perv = int
    vtor = int
    dlina_str = int(input('Какую длину строки вы желаете сгенерировать? Введите: '))
    i = 0
    while i < dlina_str:
        c.append(input('Введите значение: '))
        i += 1
    print(c)
    try:
        perv = int(c[0])
        vtor = int(c[1])
        delenie = perv / vtor
        print('Результат деления первого числа на второе: ', delenie)
    except ZeroDivisionError:
        print('Возникла ошибка при делении на 0!')
        print('Введите другие значения, пожалуйста')
    except ValueError:
        print('Нельзя делить буквы на цифры и наоборот! Введите другие значения,пожалуйста')
    else:
        print('Никаких ошибок обнаружено не было!')
        break
