magazin = {"торт": [ ['Мука,соль'],5, 200], "пирожное": [['Сахар,вода'],6, 180], "маффин": [['Шоколад,мука'],7, 540]}
for key in magazin:
    print(key, '-', magazin[key][1], '$', '-', magazin[key][2])
a = input('Введите что вы хотите получить:(описание,цена,кол-во,все) ')
if a == 'описание':
    for key,value in magazin.items():
            print(f'{key} - {value[0]}')
elif a == 'цена':
    for key,value in magazin.items():
            print(f'{key} - {value[1]}','$')
elif a == 'кол-во':
    for key,value in magazin.items():
            print(f'{key} - {value[2]}')
elif a == 'все':
    for key,value in magazin.items():
        print(f'{key} - описание:{value[0]} , цена:{value[1]} "$" ,кол-во: {value[2]}')
cena = 0
c = []
while  True:
    nazv = input('Введите название товара(торт,пирожное,маффин) или "x" для выхода из программы:')
    if nazv == 'x':
        break
    print('В наличии есть', magazin[nazv][2], 'грамм')
    kol = int(input('Введите кол-во желаемого товара:'))
    print('Цена выбранных товаров:', cena + (kol * magazin[nazv][1])/100, '$')
    magazin[nazv][2] = magazin[nazv][2] - kol
    print('В магазине осталось: торт -', magazin['торт'][2], 'пирожное -', magazin['пирожное'][2], 'маффин -',
          magazin['маффин'][2])
    cena = cena + kol * magazin[nazv][1]
    print('Для выхода из программы нажмите кнопку "x"')
    print('-------------------------------------------------------------')
print('До свидания!!!')
