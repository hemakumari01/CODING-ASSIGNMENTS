#Handle the Arithmetic exception using try-catch block
try:
    num1=10
    num2=0
    res= num1/num2
    print("Result:", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
