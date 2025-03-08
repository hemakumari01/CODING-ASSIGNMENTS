# Matching a String Against a Regular Expression With matches()
import re

pat=r"\d{3}-\d{2}-\d{4}"  
s=input("Enter a string: ")

if re.fullmatch(pat,s):
    print("Valid format!")
else:
    print("Invalid format!")
