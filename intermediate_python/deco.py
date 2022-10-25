#decorator - extending the functionality of a function

import functools

def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

def print_name():
    print('Thanh')

print_name1 = start_end_decorator(print_name)

# print_name1()

# the quivalent of the above is below

@start_end_decorator
# def print_name():
#     print('Thanh')
def add5(x):
    return x + 10
# this result will not save the output 20, because
# add5(x) is actually run by the decorator, which doesn't save
# the ouput, it just returns the wrapper

# a = add5(10)


# the identity of the add5 function is changed because it is in the decorator
# to help maintain the identity we need functool decorator
# @functools.wrap(func)

# print(help(add5))
# print(add5.__name__)


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                result = func(*args)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')

x = greet('thanh')