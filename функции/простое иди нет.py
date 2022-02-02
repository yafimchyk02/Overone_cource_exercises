def is_prime(arg):
    if arg == 2 or arg == 3 or arg == 5:
        return 'True'
    elif arg % 2 != 0 and arg % 3 != 0  and arg % 5 != 0:
        return 'True'
    else:
        return 'False'

print(is_prime(int(input('Введите число: '))))


