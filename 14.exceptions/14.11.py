try:
    with open("non_existent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("IOException Occurred: File not found!", e)

try:
    with open("/root/protected_file.txt", "w") as f:
        f.write("Test data")
except PermissionError as e:
    print("IOException Occurred: Permission denied!", e)
