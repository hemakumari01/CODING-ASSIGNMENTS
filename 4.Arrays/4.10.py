#function to find the duplicate values of an array
n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

duplicates=[]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate values:", duplicates if duplicates else "No duplicates found")
