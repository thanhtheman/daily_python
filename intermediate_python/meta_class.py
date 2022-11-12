# class Hi:
#     pass
# print(type(Hi))
# print(type(Hi()))

class Foo:
    def show(self):
        print("Hi")    

def add_attribute(self):
    self.z = 9

test = type('Hi', (Foo,), {"x": 7,"add_attribute": add_attribute})
t = test()
print(t.x)
t.add_attribute()
print(t.z)


