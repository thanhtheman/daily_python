#error and exceptions

# rasie an exception if meeting certain condition
x = -4
if x > 0:
    raise Exception('x should be positive')

#assert(condition), 'string'
assert(x < 0), 'x should be positive'

#try except, print out an error statement, finally is for clean up operation
# finally will run no matter what
try:
    b = 10 / 0
    print(b)
except Exception as e:
    print(str(e))
else:
    print('everything is ok!')
finally:
    print('I will print no matter what')


#defining our own error
class lowValueError(Exception):
    pass

def test_value(x):
    if x < 100:
        raise lowValueError('Value is too low')

try:
    test_value(10)
except lowValueError as e:
    print(str(e))