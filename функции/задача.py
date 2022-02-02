    if x >= -5 and x <= 5:
        def func(x):
            return x ** 2

    elif x < - 5:
        def func_2(x):
            return 2 * abs(x) - 1
    elif x > 5:
        def func_3(x):
            return 2 * x


func()
func_2()
func_3()