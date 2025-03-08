# function to reverse an array of integer values
def reverse_array(arr):
    n=len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1]=arr[n-i- 1],arr[i]
    return arr

n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

arr=reverse_array(arr)

print("Reversed array:", arr)
