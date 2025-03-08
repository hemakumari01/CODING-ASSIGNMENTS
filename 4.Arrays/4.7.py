# function to insert an element at a specific position in the array

def insert_arr(arr,ele,index):
    if index<0 or index>len(arr):
        print("Invalid position")
        return arr

    a=[]
    for i in range(len(arr)+1):
        if i<index:
            a.append(arr[i])
        elif i==index:
            a.append(ele)
        else:
            a.append(arr[i-1])

    return a

n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

new_element=int(input("Enter the element to insert: "))
index=int(input("Enter the position: "))

arr = insert_arr(arr, new_element, index)

print("Array after insertion:", arr)
