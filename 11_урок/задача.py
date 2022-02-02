import random

a = tuple([random.randint(1,6) for l in range(10)])
b = tuple([random.randint(-5,0) for i in range(10)])
c = a + b
print(c,'а кол-во нулей = ', c.count(0))