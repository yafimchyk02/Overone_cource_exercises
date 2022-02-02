a = [1,3,5,6,7,4,6,8,9,14,67,85,6,5,3,5,3]
b = []
for i in a:
    if a.count(i) > 2 and i not in b:
        b.append(i)
print(b)

