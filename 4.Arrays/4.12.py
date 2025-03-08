#method to remove duplicate elements from an array
n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

unique_arr=[]

for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)

print("Array after removing duplicates:", unique_arr)
