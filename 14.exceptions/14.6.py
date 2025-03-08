class AgeError(Exception):
    def __init__(self, msg="Age must be 18 or above."):
        self.msg = msg
        super().__init__(self.msg)

def chk_age(a):
    if a < 18:
        raise AgeError(f"Access Denied: {a} is too young!")  # Raising the custom exception
    else:
        print("Access Granted!")

a = int(input("Enter age: "))

chk_age(a)
