y = [1,2,3,'a','b','c',4,5,6]
c = str(y)
for i in c:
    if i.isalpha():
        print('Hi')
    elif i.isdigit():
        print('Hello')