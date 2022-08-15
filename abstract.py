from abc import ABC, abstractmethod

class Automobile(ABC):
    @abstractmethod
    def turn_on_engine(self):
        pass
    def brake_system(self):
        pass

class Toyota(Automobile):
    def turn_on_engine(self):
        print('Press the button')
    
    def brake_system(self):
        print('Normal hydraulic brake')

class BMW(Automobile):
    def turn_on_engine(self):
        print('Say TURN ON')
    def brake_system(self):
        print('Smart Brake')

a = Toyota()
a.turn_on_engine()
b = BMW()
b.brake_system()