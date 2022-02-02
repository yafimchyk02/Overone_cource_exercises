my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except (
IndexError, KeyError):  # Это не самый лучший способ, потому что, не всегда понятно, какая именно ошибка произошла
    print('Возникла ошибка IndexError or KeyError!')
