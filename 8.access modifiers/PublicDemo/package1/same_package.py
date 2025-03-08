# package1/same_package.py
from package1.parent import Parent

class SamePackage:
    def access_public(self):
        obj = Parent()
        print(obj.public_var)  # Accessing public variable
        obj.public_method()    # Calling public method

