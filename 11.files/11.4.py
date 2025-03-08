# program to read a file stream supports random access
f="sample.txt"
with open(f, "w") as file:
    file.write("This is a sample file.\nIt contains multiple lines.\n")

with open(f, "r") as file:
    print("Reading the first 10 characters:")
    print(file.read(10))  

    print("\nCurrent file position:", file.tell())  

    file.seek(5)  
    print("\nReading from position 5:")
    print(file.read(10))  

    file.seek(0)  
    print("\nReading the first line:")
    print(file.readline().strip())  
