class Student:
    def __init__(self, name, age, grade):  
        self.name=name      
        self.age=age     
        self.grade=grade    
    
    def display(self):  
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


student1=Student("Alice",20,"A")


print("Accessing attributes directly:")
print("Name:",student1.name)
print("Age:",student1.age)
print("Grade:",student1.grade)


print("\nCalling the display method:")
student1.display()
