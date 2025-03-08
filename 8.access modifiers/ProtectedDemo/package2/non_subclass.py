# package2/non_subclass.py
from package1.parent import Parent

class NonSubclass:
    def access_protected(self):
        obj = Parent()
        # Attempting to access protected members from a non-subclass
        try:
            print(obj._protected_var)  # This should still work (not strictly private)
            obj._protected_method()    # This should still work (not strictly private)
        except AttributeError:
            print("Cannot access protected members from a non-subclass in a different package")

