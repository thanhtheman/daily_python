x = [1, 2, 3]
print(x*3)

class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'{self.name} is here because I was programmed to print out the name'

p = Person('Thanh')

print(p)

from queue import Queue as q
import inspect

class New_Queue(q):
    def __repr__(self):
        return f'Queue length is: {self._qsize()}'
    def __add__(self, item):
        self.put(item)

a = New_Queue()
a + 9
a + 10
print(a)