# package2/child.py
from package1.parent import Parent

class Child(Parent):  # Inheriting Parent class
    def access_protected(self):
        print(self._protected_var)  # Accessing protected variable in subclass
        self._protected_method()    # Calling protected method in subclass

