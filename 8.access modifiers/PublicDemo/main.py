# main.py
from package1.same_package import SamePackage
from package2.different_package import DifferentPackage

print("Accessing public members within the same package:")
same_package_obj = SamePackage()
same_package_obj.access_public()

print("\nAccessing public members from a different package:")
diff_package_obj = DifferentPackage()
diff_package_obj.access_public()
