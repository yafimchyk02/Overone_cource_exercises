sl = {
    'торт' : ['состав_торта', 100 , 100 ],
    'пирожное' : ['состав_пирожка' , 50, 50]
}
a = input('Введите что вы хотите получить:описание,цена,кол-во')
# a1 = a[:a.index('-')]
# a2 = a[a.index('-')+1:]
# print(a1,a2)
if a == 'описание':
    for key,value in sl.items():
            print(f'{key} : {value[0]}')
elif a == 'цена':
    for key,value in sl.items():
            print(f'{key} : {value[1]}')
elif a == 'кол-во':
    for key,value in sl.items():
            print(f'{key} : {value[2]}')
for key,value in sl.items():
    print(f'{key} - описание:{value[0]} , цена:{value[1]},кол-во: {value[2]}')
