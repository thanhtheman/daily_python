from abc import ABC, abstractmethod

# class Automobile(ABC):
#     @abstractmethod
#     def turn_on_engine(self):
#         pass
#     def brake_system(self):
#         pass

# class Toyota(Automobile):
#     def turn_on_engine(self):
#         print('Press the button')
    
#     def brake_system(self):
#         print('Normal hydraulic brake')

# class BMW(Automobile):
#     def turn_on_engine(self):
#         print('Say TURN ON')
#     def brake_system(self):
#         print('Smart Brake')

# a = Toyota()
# a.turn_on_engine()
# b = BMW()
# b.brake_system()

class Bank(ABC):
    @abstractmethod
    def basicinfo(self):
        print('This is a generic bank')
        return 'Generic Bank: 0'
    def withdraw(self, withdraw_amount):
        pass

class Swiss(Bank):
    def __init__(self):
        self.bal = 1000
    
    def basicinfo(self):
        print('This is the Swiss Bank')
        return 'Swiss Bank: {0}'.format(self.bal)

    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal -= amount
            print('Withdrawn amount: {0}'.format(amount))
            print('New Balance: {0}'.format(self.bal))
        else:
            print('Insufficient funds')
            return self.bal
        
        return self.bal

s = Swiss()
print(s.basicinfo())
s.withdraw(30)
s.withdraw(1000)