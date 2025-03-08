def divide_numbers():
    try:
        num1=int(input("Enter first number: "))
        num2=int(input("Enter second number: "))
        res=num1/num2  
        print("Result:",res)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.") 
    except ValueError:
        print("Error: Invalid input. Please enter integers only.") 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  


divide_numbers()
