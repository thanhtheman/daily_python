from collections import namedtuple, OrderedDict, defaultdict, deque

Point = namedtuple('Point', 'x,y')
pt = Point(1,5)
# print(pt)
# print(pt.x, pt.y)

# dictionary = OrderedDict()
dictionary = defaultdict(int)
dictionary['a'] = 8
dictionary['b'] = 15
dictionary['c'] = 12
dictionary['d'] = 85
dictionary['e'] = 18
# print(dictionary)
# print(dictionary.keys())

d = deque()

d.append(1)
d.append(2)
d.appendleft(4)

print(d)
print(list(d)[0])

d.popleft()
d.extend([45,47,89])

print(d)

d.extendleft([56,89,100])
print(d)
d.rotate()
print(d)