class Example:
    def display(self,value):  
        if isinstance(value,int):
            print(f"Integer Value: {value}")
        elif isinstance(value,str):
            print(f"String Value: {value}")
        else:
            print("Unsupported data type!")

obj = Example()

obj.display(10)

obj.display("Python")
