import time

def func(f):
    def wrapper(*args, **kwargs):
        print('Started')
        result = f(*args, **kwargs)
        print('Ended')
        return result
    return wrapper

@func
def func2(x):
    print(f'I am func2 {x}')
    return x

def func3():
    print('I am func3')

#when we call func2, actually we are calling wrapper()
# thus just make sure wrapper have the same arguments as func2

# a = func2(10)
# print(a)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print('Time: ', total)
        return rv
    return wrapper

@timer
def test():
    time.sleep(2)

test()
