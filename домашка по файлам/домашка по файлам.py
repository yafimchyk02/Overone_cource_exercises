c = []
b = []
chisla = []
slova = []
i = 0
f = open('text.txt', 'r')
for k in f:
    c.append(k)
#print(c)
while i < len(c):
    if i < len(c) - 1:
        b.append(c[i][0:-1])
    else:
        b.append(c[i][0:])
    i += 1
print(b)

for j in b:
    if j.isdigit():
        chisla.append(int(j))
    else:
        slova.append(j)
chisla.sort()
slova.sort()
print(chisla + slova)
f.close()


