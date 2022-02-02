def schet (a):
    g = 0
    s = 0
    glasni = ['А','а','О','о','Э','э','Е','е','И','и','Ы','ы','У','у','Ё','ё','Ю','ю','Я','я']
    for i in a:
        for l in glasni:
            if i == l:
                g += 1
            elif l != i and ' ' in a:
                s = len(a) - g - a.count(' ')
            elif l != i and ' ' not  in a:
                s = len(a) - g


    return g,s
print(schet(input('Введите строку: ')))

