#Define a static variable and access that through a instance
class Example:
    static_var=100  # Static variable

# Creating an instance of the class
obj=Example()

# Accessing the static variable through an instance
print("Accessing through instance:",obj.static_var)

# Modifying the static variable using the instance
obj.static_var=200  # This creates an instance variable, not modifying the class variable

# Accessing again through instance and class
print("After modification through instance:",obj.static_var)  # This refers to the instance variable now
print("Accessing through class:",Example.static_var)  # The class variable remains unchanged
