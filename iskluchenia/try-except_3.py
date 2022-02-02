my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except IndexError:
    print('Такого индекса не существует!')
except KeyError:
    print('Такого ключа нет в словаре!')
except:
    print('Возникла другая ошибка!')
