class Example:
    def add(self,a,b=None):  
        if b is not None: 
            print(f"Sum of {a} and {b}: {a + b}")
        else:  
            print(f"Value: {a}")


obj = Example()

obj.add(5)

obj.add(5, 10)
