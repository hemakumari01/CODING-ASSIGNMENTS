# program to remove the duplicate elements and return the new array
n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

new_arr=[]

for num in arr:
    if num not in new_arr:
        new_arr.append(num)

print("Array after removing duplicates:", new_arr)
