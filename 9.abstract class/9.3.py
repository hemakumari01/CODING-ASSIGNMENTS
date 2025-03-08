from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):

    def start_engine(self):
        print("Car engine started.")
    def create_instance(self):
        car_obj = Car() 
        car_obj.start_engine() 

c = Car()
c.create_instance()  
