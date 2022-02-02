def kvadrat(storona):
    p = storona * 4
    s = storona ** 2
    d = ((storona ** 2) * 2) ** 0.5
    d = float('{:.1f}'.format(d))
    return p,s,d

print(kvadrat(int(input('Введите сторону кадрата: '))))
