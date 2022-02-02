def mul(a):
    def helper(b):
        return a * b

    return helper

print(mul(3)(2))