a = [5,[1,2],2,'r',4,'ee']
b = [4,'ww','ee',3,[1,2]]
list = []
for i in a:
    for k in b:
        if i == k:
            list.append(i)
print(list)
            