class Parent:
    def __init__(self):
        self.__private_field ="I am private!"

    def __private_method(self): 
        print("This is a private method.")

    def access_private(self):
        print("Accessing private field inside the class:", self.__private_field)
        self.__private_method()

class Child(Parent):
    def show(self):
        try:
            print("Trying to access private field from subclass:", self.__private_field)
        except AttributeError:
            print("Cannot access private field from subclass.")

        try:
            self.__private_method()
        except AttributeError:
            print("Cannot access private method from subclass.")


if __name__ == "__main__":
    obj = Parent()
    obj.access_private()  

    child_obj = Child()
    child_obj.show() 
