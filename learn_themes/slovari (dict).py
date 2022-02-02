import random
d = dict(short = 'dict',long = 'dictionary')
d_1 = dict([(1,2),(2,3)])

d_2 = dict.fromkeys(['a','b'],100)
print(d_2)
d_3 = {a:random.randint(1,10) for a in range(7)}
print(d_3)
print(len(d_3))