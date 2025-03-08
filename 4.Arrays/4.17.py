#method to verify if the array contains two specified elements(12,23)
n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

found_12=False
found_23=False

for num in arr:
    if num==12:
        found_12=True
    if num==23:
        found_23=True

if found_12 and found_23:
    print("The array contains both 12 and 23.")
else:
    print("The array does not contain both 12 and 23.")
