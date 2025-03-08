
class Example:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor: No arguments passed.")
        elif arg2 is None:
            print(f"One-Argument Constructor:arg1={arg1}")
        else:
            print(f"Two-Argument Constructor:arg1 ={arg1},arg2={arg2}")

class Main:
    def __init__(self):
        print("\nCalling Default Constructor:")
        obj1=Example()

        print("\nCalling One-Argument Constructor:")
        obj2=Example(10)

        print("\nCalling Two-Argument Constructor:")
        obj3=Example(20, "Python")

if __name__=="__main__":
    Main()
