#Write a program to read a file stream
f="output.txt" 

try:
    with open(f, "r") as file:
        print("File content:")
        for line in file:
            print(line, end="")  
except FileNotFoundError:
    print(f"Error: The file '{f}' was not found.")
