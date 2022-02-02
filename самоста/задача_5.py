songsdict = {

    'World in My Eyes': 4.76,

    'Sweetest Perfection': 5.43,

    'Personal Jesus': 4.56,

    'Halo': 4.30,

    'Waiting for the Night': 6.07,

    'Enjoy the Silence': 4.6,

    'Policy of Truth': 4.88,

    'Blue Dress': 4.18,

    'Clean': 5.68,

}
sum = 0
bolsept = []
for i in songsdict.values():
    sum = sum + i
for i in songsdict.keys():
    if songsdict[i] > 5:
        bolsept.append(i)
key = []
value = []
for i in songsdict.keys():
    if ' ' not in i:
        key.append(i)
        value.append(songsdict[i])
d = zip(key,value)



print('общее время:', sum)
print(bolsept)
print(list(d))

