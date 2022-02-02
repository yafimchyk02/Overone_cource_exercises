b = ['l', 'P', 'k', 'o', 'r', 't']
zn = 0
verh = []
niz = []
while zn + 1 < len(b):
    zn = zn + 1
    for i in b:
        if b[zn].isupper() and b[zn + 1].isupper():
            verh.append(zn)
        elif b[zn].islower() and b[zn + 1].islower():
            niz.append(zn)
print(len(verh))
print(len(niz))
