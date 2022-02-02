glasni = ('a', 'e', 'i', 'o', 'u', 'y')
soglasni = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's','t', 'v', 'w', 'x', 'z')
sog = []
gla = []
list = [15, 48, 'hello', 6, 19, 'world']
for i in list:
    sog.clear()
    gla.clear()
    if type(i) is str:
        b = ''.join(i)
        print(b)
        for l in b:
            if l in glasni:
                gla.append(l)
            elif l in soglasni:
                sog.append(l)
        print('Найдено слово',i,' кол-во гласных',len(gla),'кол-во согласных',len(sog))


