d = {1:2,2:4,3:9}
d[4] = 4 ** 2
print(d[1])
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(len(d))
print(d.pop(1,))
print(d)
del d[2]
print(d)
if 3 in d:
    del d[3]
    print(d)