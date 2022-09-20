def divide_by(a,b):
    return a/b

try:
    ans = divide_by(4,0)
except Exception as e:
    print('Something went wrong!', e.__class__)


def less_than(a,b):
    if a < b:
        return a
    else:
        return b or a


def cube(x):
    return x**3

print(cube(-4))