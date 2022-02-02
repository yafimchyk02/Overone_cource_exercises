a = 'An apple a day keeps the doctor away'
values = []
keys = []
d = {}
for i in a:
    keys.append(i)
    values.append(a.count(i))
d = zip(keys,values)
print(list(d))
