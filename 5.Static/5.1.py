class Example:
    static_var=100  
# Accessing static variable using class name
print("Accessing through class:",Example.static_var)
# Creating an object and accessing the static variable
obj=Example()
print("Accessing through object:",obj.static_var)
# Modifying the static variable through the class
Example.static_var=200
print("After modification through class:", Example.static_var)
# Creating another object to check if it reflects the change
obj2=Example()
print("Accessing through another object:", obj2.static_var)
