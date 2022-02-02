try:
    k = 1 / 0
except ZeroDivisionError:  # Зная, какие существуют исключения, можно их обрабатывать (невелировать)
    k = 0
print(k)
print()

try:
    k = 1 / 0
except ArithmeticError:  # ArithmeticError покрывает сразу несколько ошибок, включая ZeroDivisionError
    k = 0
print(k)
