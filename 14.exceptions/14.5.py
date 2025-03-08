def check_age(age):
    if age < 18:
        raise ValueError("Access Denied: You must be 18 or older.")  
    else:
        print("Access Granted!")

user_age = int(input("Enter your age: "))
check_age(user_age)
