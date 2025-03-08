# main.py
from package1.same_package import SamePackage
from package2.child import Child
from package2.non_subclass import NonSubclass

print("Accessing protected members within the same package:")
same_package_obj = SamePackage()
same_package_obj.access_protected()

print("\nAccessing protected members from a child class in a different package:")
child_obj = Child()
child_obj.access_protected()

print("\nAttempting to access protected members from a non-subclass in a different package:")
non_subclass_obj = NonSubclass()
non_subclass_obj.access_protected()
