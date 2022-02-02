a = ["кот","слон","змея"]
b = a.copy()
b.append(6)
print(a,b)

d = list(a)
print(a,d)

import copy

e = copy.copy(a)
e.append(5)
print(a,e)

f = copy.deepcopy(a)
f.append(5)
print(a,f)

c = a[:] # устаревший синтаксис
print(a,c)