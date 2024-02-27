# standart decorator function!
def outer(func):
    def inner(*args):
        result = func(*args)
        return result

    return inner
