#Write a program to check whether a file is having read access and write access permissions
import os

f="sample.txt" 

if os.path.exists(f):
    if os.access(f, os.R_OK):
        print(f"File '{f}' has read access.")
    else:
        print(f"File '{f}' does NOT have read access.")

    if os.access(f, os.W_OK):
        print(f"File '{f}' has write access.")
    else:
        print(f"File '{f}' does NOT have write access.")
else:
    print(f"Error: The file '{f}' does not exist.")
