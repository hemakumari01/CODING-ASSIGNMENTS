#Write a program to read a file a just to a particular index using seek()
f="sample.txt"

try:
    with open(f, "r") as file:
        print("Reading first 10 characters:")
        print(file.read(10))  

        print("\nUsing seek() to move to index 5...")
        file.seek(5)  
        print("Reading from index 5:")
        print(file.read(10))  

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
