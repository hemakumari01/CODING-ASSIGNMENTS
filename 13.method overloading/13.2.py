class Example:
    def display(self,*args):  
        if len(args)==1 and isinstance(args[0],int):
            print(f"Integer Value: {args[0]}")
        elif len(args)==1 and isinstance(args[0],str):
            print(f"String Value: {args[0]}")
        elif len(args)==2 and isinstance(args[0],int) and isinstance(args[1], float):
            print(f"Integer: {args[0]}, Float: {args[1]}")
        else:
            print("Invalid arguments!")

obj = Example()

obj.display(10)

obj.display("Python")

obj.display(5, 10.5)
