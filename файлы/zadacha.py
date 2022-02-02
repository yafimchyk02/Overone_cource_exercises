f = open('числа.txt', 'r')
l = f.readlines()
print(l)
for i in l:
    i = i.replace('_', '')
    c = i.split('')
print(c)
sum = 0
for i in c:
    if i.isdigit():
        i = int(i)
        sum += i
print(sum)
