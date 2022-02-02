a = int(input("Введите порядковый номер пальца"))
print(a)
if a == 1:
    print('Вы указали большой палец')
elif a == 2:
    print('Указательный')
elif a == 3:
    print('Средний')
elif a == 4:
    print('Безымянный')
elif a == 5:
    print('Мизинец')
else:
    print('Нет соответсвия')