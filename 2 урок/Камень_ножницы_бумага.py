import random

nozhnicy = 1
kamen = 2
bumaga = 3

print('nozhnicy = 1,','kamen = 2,','bumaga = 3') # Пользователь видит диапазон выбора

a = int(input('Выберите число от 1 до 3'))
print('Камень - Ножницы - Бумага')
if a == 1:
    print("Вы выбрали ножницы")
elif a== 2:
    print("Вы выбрали камень")
elif a== 3:
    print("Вы выбрали бумагу")
else:
    print("Неверное число")

b = random.randint(1,3)  # Компютер делает ход
if b == 1:
    print("Компьбтер выбрал ножницы")
elif b== 2:
    print("Компьютер выбрал камень")
elif b== 3:
    print("Компьютер выбрал бумагу")

# Сравнение ходов компьютера и игрока

if a == b:                        # Если пользователь выбрал ножницы
    print("Ничья")
elif a < b and b == 2 and a == 1:
    print("Вы проиграли")
elif a < b and b == 3 and a == 1:
    print("вы выйграли")

if a == b:
    print("Ничья")
if a > b and b == 1 and a == 2:  # Если пользователь выбрал камень
    print("Вы выйграли")
elif a < b and b == 3 and a == 2:
    print("Вы проиграли")

if a == b:
    print("Ничья")
if a > b and b == 1 and a == 3:   # Если пользователь выбрал бумагу
    print("Вы проиграли")
elif a > b and b == 2 and a == 3:
    print("Вы выйграли")








