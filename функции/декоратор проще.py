def simple_decore(fn):
    print('Syart function')

    fn()
    print('Stop function')

@simple_decore
def first_test():
    print('Test function 1')