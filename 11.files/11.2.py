#Write a program to write text to .txt file using  InputStream
f="output.txt"

with open(f, "w") as file:
    print("Enter text to write into the file. Type 'STOP' to end input:")

    while True:
        line = input()  
        if line == "STOP": 
            break
        file.write(line + "\n")  

print(f"Text successfully written to {f}")

