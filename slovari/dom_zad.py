magazin = {"apple": [5, 20], "orange": [6, 18], "pear": [7, 54], "strawberry": [10, 230]}
for key in magazin:
    print(key, '-', magazin[key][0], '$', '-', magazin[key][1])
nazv = input('Введите название продукта')
for i in magazin.keys():
    print(i)