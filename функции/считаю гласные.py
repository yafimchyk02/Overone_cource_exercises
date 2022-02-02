def schet(a):
    g = 0
    sog = 0
    glasni = ['А', 'а', 'О', 'о', 'Э', 'э', 'Е', 'е', 'И', 'и', 'Ы', 'ы', 'У', 'у', 'Ё', 'ё', 'Ю', 'ю', 'Я', 'Я']
    for i in a:
        for l in glasni:
            if i == l:
                g += 1
    return g
print(schet(input('Введите строку: ')))
