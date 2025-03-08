# package1/same_package.py
from package1.parent import Parent

class SamePackage:
    def access_protected(self):
        obj = Parent()
        print(obj._protected_var)  # Accessing protected variable
        obj._protected_method()    # Calling protected method

