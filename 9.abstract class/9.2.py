from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

    def fuel_status(self):
        print("Fuel level is sufficient.")

class Car(Vehicle):

    def start_engine(self):
        print("Car engine started.")

car_obj = Car()

car_obj.start_engine()

car_obj.fuel_status()
