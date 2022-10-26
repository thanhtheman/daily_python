# the problem: not enough memory to run this things
# at 10,000, it takes a while for the computer to run
# at 1,000,000 the computer is frozen

#-------------------------------------
# x = [i**2 for i in range(1000000000)]
# print(x)
#------------------------------------

# To free up memory, we can do this: not saving every number in a list
# this line of code will do exactly the same, things are getting better
# the computer doesn't get frozen, it just keep printing!

#-------------------------------------
# for i in range(1000000):
#     print(i)
#-------------------------------------

# Or we can try the generator idea

#-------------------------------------
class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv

g = Gen(10000)

# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break
#-------------------------------------

# Or we can try the generator idea with the "yield" command
# it is kind of like "pausing", instead of "stopping"


def gen(n):
    for i in range(n):
        yield i**2
        print('paused for now')
        

a = gen(10)

import sys

print(a)
#a is a <generator object gen at 0x000001D6F0904270>

#-------------------------------------
# for i in a:
#     print(i)
#-------------------------------------

# there is still one more way to print the value

#-------------------------------------
# print(next(a))
# print(next(a))
#-------------------------------------


# measure the memory used by this generator and the traditional
# saving everything in the list
import sys
b = gen(100000)
x = [i ** 2 for i in range(100000)]
print(sys.getsizeof(b))
print(sys.getsizeof(x))