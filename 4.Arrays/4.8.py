#function to find the minimum and maximum value of an array
def min_max(arr):
    if not arr:
        return "Array is empty"

    min_v=arr[0]
    max_v=arr[0]
    for num in arr:
        if num<min_v:
            min_v=num
        if num>max_v:
            max_v=num
    return min_v,max_v

n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    num=int(input())
    arr.append(num)

min_v,max_v=min_max(arr)
print("Minimum value:",min_v)
print("Maximum value:",max_v)
