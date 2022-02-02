words = dict()
count = int(input("Кол-во слов в словаре"))

i = 0
while i < count:
    print('Ввод слов')
    wrd = str(input('Слово:'))
    value = int(input('Значение:'))

    if wrd not in words:
        words[wrd] = value
        i += 1
print(words)
