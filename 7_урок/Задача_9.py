a = (input('Введите строку, состоящую из разных регистров: '))
print('Ваша строка: ',a)
b = []
for i in a:
    if i.islower():
        b.append(i)
c = ''.join(b)

print('Строка без букв верхнего регистра: ',c)

