#function to get the difference of largest and smallest value
def find_difference(arr):
    if not arr:
        return "Array is empty"

    min_val=arr[0]
    max_val=arr[0]

    for num in arr:
        if num<min_val:
            min_val=num
        if num>max_val:
            max_val=num

    return max_val-min_val

n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

difference=find_difference(arr)
print("Difference between largest and smallest value:", difference)
