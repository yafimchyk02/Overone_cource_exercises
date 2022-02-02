def decore (fn):
    def wrapper():
        print('Start function')

    fn()

    print('Stop function')
    return wrapper()

@decore
def test():
    print('Test function')

