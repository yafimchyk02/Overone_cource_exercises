while True:
    print('Поздавляем, вы выйграли 200 000 USD! Второй впрос')  # Второй вопрос
    n = str('В каком году отмненили крепостное право?')
    print(n)
    q = int(1861)
    w = int(1456)
    e = int(1893)
    print('1.', w, '2.', q, '3.', e)
    k = int(input('Ваш ответ:'))
    if k == 1 or k == 3:
        print('Ответ неверный,начните заново')
    else:
        break

