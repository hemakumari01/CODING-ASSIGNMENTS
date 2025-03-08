#Searching in strings using index()
s=input("Enter the main string: ")  
sub=input("Enter the substring to search: ")  

try:  
    p=s.index(sub)  
    print(f"Substring found at index: {p}")  
except ValueError:  
    print("Substring not found!")  
