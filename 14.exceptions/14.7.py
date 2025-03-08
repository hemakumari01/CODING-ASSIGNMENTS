def divide_numbers():
    try:
        a=int(input("Enter first number: "))
        b=int(input("Enter second number: "))
        res=a/b 
        print("Result:", res)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")
    finally:
        print("Execution completed. Thank you!")  

divide_numbers()
