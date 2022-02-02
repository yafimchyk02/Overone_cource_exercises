a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
c = int(input('Введите третье число'))

if a > b and a > c :
    print("Первое наибольшее")
elif b > a and b > c :
    print("Второе наибольшее")
elif c > a and c > b :
    print("Третье наибольшее")
else:
    print("Наибольших несколько")