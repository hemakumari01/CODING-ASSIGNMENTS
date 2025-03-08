#Write a program to read text file
file = open("HW.txt", "r")
data = file.read()
print(data)
file.close()
