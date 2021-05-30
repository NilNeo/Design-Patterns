"""
Singleton
"""
def singleton(_class):
    __instances = {}
    
    def getInstance(*args, **kwargs):
        if _class not in __instances:
            __instances[_class] = _class(args, kwargs)
        return __instances[_class]

    return getInstance

@singleton
class Registry():
    def __init__(self, *args, **kwargs):
        self.regPath = "C:\A\B"
        self.args    = args
        self.kwargs  = kwargs

if __name__ == '__main__':
    print('*** with parameters ***')
    r1 = Registry(10, 20, 'args')
    r2 = Registry(30, 40, 'args 2')

    print(f'ID of r1: {id(r1)} with args {r1.args}')
    print(f'ID of r2: {id(r2)} with args {r2.args}')
    print(f'is r1 same as r2: {r1 is r2}')

    print('\n*** without parameters ***')
    r1 = Registry()
    r2 = Registry()

    print(f'ID of r1: {id(r1)} with args {r1.args}')
    print(f'ID of r2: {id(r2)} with args {r2.args}')
    print(f'is r1 same as r2: {r1 is r2}')

# OUTPUT
# *** with parameters ***
# ID of r1: 2102115110856 with args ((10, 20, 'args'), {})
# ID of r2: 2102115110856 with args ((10, 20, 'args'), {})
# is r1 same as r2: True

# *** without parameters ***
# ID of r1: 2102115110856 with args ((10, 20, 'args'), {})
# ID of r2: 2102115110856 with args ((10, 20, 'args'), {})
# is r1 same as r2: True