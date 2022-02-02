my_dict = {'a': 1, 'b': 2, 'c': 3}

try:
    value = my_dict['d']
except KeyError:
    print('Произошла ошибка KeyError!')
else:
    print('Ощибок не произошло!')  # else сработает только в том случае, если в нашем коде нет ни единой ошибки
