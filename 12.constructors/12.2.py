# Superclass
class Parent:
    def __init__(self,arg1=None):
        if arg1 is None:
            print("Parent Default Constructor: No arguments passed.")
        else:
            print(f"Parent Argument Constructor:arg1={arg1}")

# Subclass
class Child(Parent):
    def __init__(self, arg1=None):
        if arg1 is None:
            print("Child Default Constructor")
            super().__init__()  # Calling Parent's Default Constructor
        else:
            print(f"Child Argument Constructor: arg1 = {arg1}")
            super().__init__(arg1)  # Calling Parent's Argument Constructor

# Main Execution
print("\nCalling Child Default Constructor:")
obj1=Child()

print("\nCalling Child Argument Constructor:")
obj2=Child(50)
