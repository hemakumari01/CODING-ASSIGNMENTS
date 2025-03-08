#Define a static variable and change within the instance
class Example:
    static_var=100  # Static (class) variable

# Creating an instance
obj=Example()

# Accessing the static variable through the instance
print("Before modification:")
print("Accessing through instance:",obj.static_var)
print("Accessing through class:",Example.static_var)

# Modifying the static variable within the instance
obj.static_var=200  # This creates an instance variable, not modifying the class variable

print("\nAfter modification through instance:")
print("Accessing through instance:",obj.static_var)  # Refers to the instance variable
print("Accessing through class:",Example.static_var)  # Class variable remains unchanged

# Modifying the static variable properly (through the class)
Example.static_var=300

print("\nAfter modification through class:")
print("Accessing through instance:",obj.static_var)  # Instance variable remains unchanged
print("Accessing through class:",Example.static_var)  # Class variable is updated
