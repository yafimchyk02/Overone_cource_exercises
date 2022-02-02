a = input('Введите слово,состоящее из букв верхнего и нежнего регистра: ')
print('В слове', len(a), 'букв')
b = []
for l in a:
    b.append(l)
niz = 0
verh = 0
zn = 0
for i in b:
    zn += 1
    if b[zn].isupper() and b[zn + 1].isupper() and zn + 1 < len(a):
        verh = verh + 1
    elif b[zn].islower() and b[zn + 1].islower() and zn + 1 < len(a):
        niz = niz + 1
if niz > 0:
    print(niz, 'пара нижнего')
if verh > 0:
    print(verh, 'пар верхнего')
