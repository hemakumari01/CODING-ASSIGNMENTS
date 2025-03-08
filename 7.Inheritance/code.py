class A:
    def __init__(self):
        self.data = "Data from A"

    def method_A1(self):
        print("Method A1: Specific to Class A")

    def method_A2(self):
        print("Method A2: Specific to Class A")

    def display(self): 
        print("Display method in Class A")

class B(A):
    def __init__(self):
        super().__init__()
        self.data = "Data from B"  

    def method_B1(self):
        print("Method B1: Specific to Class B")

    def method_B2(self):
        print("Method B2: Specific to Class B")

    def display(self): 
        print("Display method in Class B (Overridden)")

class C(B):
    def __init__(self):
        super().__init__()
        self.data = "Data from C" 

    def method_C1(self):
        print("Method C1: Specific to Class C")

    def method_C2(self):
        print("Method C2: Specific to Class C")

    def display(self): 
        print("Display method in Class C (Overridden)")

class MainClass:
    @staticmethod
    def main():
        
        obj_A = A()
        obj_B = B()
        obj_C = C()

        print("\n--- Calling methods using own objects ---")
        obj_A.method_A1()
        obj_A.method_A2()
        obj_A.display()

        obj_B.method_B1()
        obj_B.method_B2()
        obj_B.display()

        obj_C.method_C1()
        obj_C.method_C2()
        obj_C.display()

        print("\n--- Calling overridden methods using superclass reference ---")
        ref_A: A = obj_B
        ref_A.display()  

        ref_A = obj_C  
        ref_A.display()
        
        print("\n--- Runtime Polymorphism with Data Members ---")
        obj_A = A()
        obj_B = B()
        obj_C = C()

        ref_A = obj_B
        print(f"Accessing data via A reference to B object: {ref_A.data}") 

        ref_A = obj_C
        print(f"Accessing data via A reference to C object: {ref_A.data}")  

if __name__ == "__main__":
    MainClass.main()
