#Define a static variable and change within the class
class Example:
    static_var=100  # Static (class) variable

# Accessing the static variable before modification
print("Before modification:")
print("Accessing through class:",Example.static_var)

# Modifying the static variable using the class name
Example.static_var=200

# Accessing after modification
print("\nAfter modification:")
print("Accessing through class:",Example.static_var)

# Creating instances and checking if the change reflects
obj1=Example()
obj2=Example()
print("\nAccessing through instances:")
print("Instance 1:",obj1.static_var)
print("Instance 2:",obj2.static_var)

