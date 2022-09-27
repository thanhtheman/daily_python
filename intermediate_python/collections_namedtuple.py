from collections import namedtuple, OrderedDict, defaultdict

Point = namedtuple('Point', 'x,y')
pt = Point(1,5)
print(pt)
print(pt.x, pt.y)

dictionary = OrderedDict()
dictionary['a'] = 8
dictionary['b'] = 15
dictionary['c'] = 12
dictionary['d'] = 85
dictionary['e'] = 18
print(dictionary)
print(dictionary.keys())

