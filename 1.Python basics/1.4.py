#the local and Global variables with the same name
#Global variable
a=10
def my_func():
    a=15 #local variable
    print("Local varible inside the 1st function:",a)
def my_func2():
    a=12
    print("Local variable inside 2nd funtion:",a)
def my_func3():
    global a
    a=5
    print("Global varibale inside 3rd function:",a)
print("Global value:",a)    
my_func()
print("Global value:",a)
my_func2()
print("Global value:",a)
my_func3()
print("Global value:",a)


