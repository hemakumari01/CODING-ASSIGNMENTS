#function to copy an array to another array
def copy_arr(org):
    copy=[]
    for item in org:
        copy.append(item)
    return copy
n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
b=copy_arr(a)
print("origianl array:",a)
print("copied array:",b)
