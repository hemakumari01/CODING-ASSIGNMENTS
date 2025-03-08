def read_file():
    file_name = "non_existent_file.txt"  
    f = open(file_name, "r")  
    print(f.read()) 

read_file()
