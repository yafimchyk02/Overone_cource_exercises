def plus(a,b):
    return a + b
def minus(a,b):
    return a - b
def umnosh(a,b):
    return a * b
def podeli(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Ошибка при делениии на ноль!')

while True:
    perv = int(input('Введите первое число: '))
    deistv = input('Выберите действие (+,-,*,/): ')
    vtor = int(input('Введите второе число: '))
    if deistv == '+':
        print(perv,'+',vtor,'=',plus(perv,vtor))
    elif deistv == '-':
        print(perv,'-',vtor,'=',minus(perv,vtor))
    elif deistv == '*':
        print(perv,'*',vtor,'=',umnosh(perv,vtor))
    elif deistv == '/' and vtor == 0:
        print(perv,'/',vtor,'=',podeli(perv,vtor))
        break
    elif deistv == '/':
        print(perv,'/',vtor,'=',podeli(perv,vtor))








