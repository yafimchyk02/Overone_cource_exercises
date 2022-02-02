my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Произошла ошибка KeyError!')
finally: # Finally выполняет блок инструкций в любом случае, независимо от исключений!
    print('Оператор finally выполнен!')