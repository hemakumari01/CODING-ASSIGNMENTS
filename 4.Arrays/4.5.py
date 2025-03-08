#a function to remove a specific element from an array
def rem_ele(arr,v):
    res=[]
    for num in arr:
        if num!=v:
            res.append(num)
    return res
n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
ele=int(input("Enter the element to remove:"))
n_arr=rem_ele(a,ele)
print(n_arr)
