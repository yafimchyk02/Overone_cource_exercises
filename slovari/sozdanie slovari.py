d = {}
d = {'dict': 1, 'dictionary': 2}
print(type(d))
print(d)
print()
print()


# 2 sposob
d = dict(short='dict', long='dictionar')
d_2 = dict([(1,2),(2,4)])
print(d, '\n',d_2)
print()
print()


# fromkeys , когда нужно присвоить одинаковое згачение нескольким ключам
d = dict.fromkeys(['a','b'])
d_2 = dict.fromkeys(['a','b'],100)
print(d, '\n',d_2)
print()
print()

# generator slovaria
d = {a: a ** 2 for a in range(7)}
print(d)
