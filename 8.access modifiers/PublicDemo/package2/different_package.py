# package2/different_package.py
from package1.parent import Parent

class DifferentPackage:
    def access_public(self):
        obj = Parent()
        print(obj.public_var)  # Accessing public variable from another package
        obj.public_method()    # Calling public method from another package

