from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass
    def sleep(self):
        print("This animal is sleeping.")

class Dog(Animal):
  
    def make_sound(self):
        print("Dog barks: Woof! Woof!")

d = Dog()
d.make_sound()  
d.sleep()  
