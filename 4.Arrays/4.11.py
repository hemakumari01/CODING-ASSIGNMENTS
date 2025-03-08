# program to find the common values between two arrays
n1=int(input("Enter the number of elements in first array: "))
arr1=[]
for i in range(n1):
    num=int(input())
    arr1.append(num)

n2=int(input("Enter the number of elements in second array: "))
arr2=[]
for i in range(n2):
    num=int(input())
    arr2.append(num)

common_values=[]

for i in arr1:
    if i in arr2 and i not in common_values:
        common_values.append(i)

print("Common values:", common_values if common_values else "No common values found")
