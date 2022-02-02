s = '1. Дарите цветы'
print(s)
d = (s.replace('Дарите цветы','Цветы дарите'))
print(d)
for i in s:
    if i == '1':
        print('Цифра 1 была заменена на "one": ',s.replace('1','one'))



