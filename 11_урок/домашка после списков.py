import math
glasni = ('a', 'e', 'i', 'o', 'u', 'y')
soglasni = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's','t', 'v', 'w', 'x', 'z')

list = [15, 48, 'hello', 6, 19, 'world']
print('список первоначальный: ', list)
for i in list:
    if type(i) is int and i % 2 == 0 and i > 10:
        print('Число', i, 'четное, сумма его цифр: ', (i // 10) + (i - 10*(i // 10)))
    elif type(i) is int and i % 2 != 0 and i > 10:
        ind = list.index(i)
        list[ind] = 1
        print('Число',i,'нечетное,заменяю его на "1" в списке: ',list)
    elif type(i) is int and i < 10 and i % 2 == 0:
        print('Найдена цифра: ',i,','"она чётная")
    elif type(i) is int and i < 10 and i % 2 != 0:
        print('Найдена цифра:', i,',' "она нечётная")
print('После работы с числами имеем список: ',list)


sog = []
gla = []
list = [15, 48, 'hello', 6, 19, 'world']
for i in list:
    sog.clear()
    gla.clear()
    if type(i) is str:
        b = ''.join(i)
        for l in b:
            if l in glasni:
                gla.append(l)
            elif l in soglasni:
                sog.append(l)
        print('Найдено слово:',i,' кол-во гласных:',len(gla),'кол-во согласных:',len(sog))
