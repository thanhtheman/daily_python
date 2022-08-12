#BASIC
# class Recipe:
#     def __init__(self, name, items, time):
#         self.name = name
#         self.items = items
#         self.time = time

#     def content(self):
#         print(self.name + ' has ' + str(self.items) + ' and it takes ' + \
#         str(self.time) + ' min to prepare')
#         return 'ok'

# pizza = Recipe('Pizza', ['chesse', 'veggie', 'meat', 'pineapple'], 45)
# pasta = Recipe('Pasta', ['noodle', 'sea food', 'sauce', 'cheese'], 15)

# print(pizza.content())

# class Paymentslips:
#     def __init__(self, name, status, amount) -> None:
#         self.name = name
#         self.status = status
#         self.amount = amount
#     def pay(self):
#         self.status = 'yes'
#     def check_status(self):
#         if self.status == 'yes':
#             return self.name + ' has been paid '+ str(self.amount)
#         else:
#             return self.name + ' has not been paid yet'

# david = Paymentslips('David', 'no', 2000)
# lucas = Paymentslips('Lucas', 'no', 3000)
# print(lucas.check_status())
# lucas.pay()
# print(lucas.check_status())


#PARENT AND CHILD
class Employees:
    a = 10
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
class Chefs(Employees):
    def leave_request(self, days):
        return 'I want to take ' + str(days) + ' off'

david = Employees('David', "Foo")
lucas = Supervisors('Lucas', 'Toni', 'apple')
emily = Chefs('Emily', 'Zhue')

# print(david.last)
# print(lucas.password)
# print(emily.leave_request(5))
# print(issubclass(Supervisors, Chefs))
# print(isinstance(david,Chefs))

object = {
    'captain': 'lucas',
    'pirate': 'david' 
}

print(david)