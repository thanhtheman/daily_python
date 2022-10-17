# this is a shorter way to write a function, like arrow function in JS
#lambda arguments: expression
multiply20 = lambda i, y: i*y*20
result = multiply20(2,10)
# print(result)

#sorting things with a lambda function as a key
points =[(1, 2), (15, 1), (5, -1), (10, 4)]
sort_x = sorted(points)
sort_y = sorted(points, key=lambda i: i[1])
sort_by_sum = sorted(points, key=lambda i: i[0] + i[1])

# print(sort_x)
# print(sort_y)
# print(sort_by_sum)

#map(func, seq)
a = [1, 2, 3, 4, 5]
b = map(lambda i: i*2, a)
print(list(b))
c = [i*2 for i in a]
print(c)

#filter(func, seq)
d = filter(lambda i: i%2 == 0, a)
e = [i for i in a if i%2 == 0]
print(list(d))

#reduce(func, seq)
from functools import reduce
f =  reduce(lambda x,y: x*y, a)
print(f)