# a function to test if array contains a specific value
def arr_con(arr,v):
    for num in arr:
        if num==v:
            return True
    return False
n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
ele=int(input("Enter the element:"))
if arr_con(a,ele):
    print("Element found")
else:
    print("Element not found")
