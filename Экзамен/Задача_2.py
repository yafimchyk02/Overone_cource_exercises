glasni = ['А','а','Е','е','Ё','ё','О','о','И','и','У','у','Ы','ы','Э','э','Ю','ю','Я','я']
# Остальные буквы согласные
b = 0
g =[]
s =[]
a = input('Введите какой либо текст: ')
for i in a:
    for l in glasni:
        if i == l:
            g.append(i)
        else:
            s.append(i)
            for n in s:
                if s.count(n) > 1:
                    s.remove(n)
print('Кол-во гласных: ',len(g))
print('Кол-во согласных: ', len(s)-len(g))

if len(g)==len(s)-len(g):
    b = ''.join(g)
print(b)
