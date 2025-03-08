# program to find the index of an array element
n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
ele=int(input("enter the element:"))
f=False
for i in range(n):
      if a[i]==ele:
        print("Index is:",i)
        f=True
        break
if not f:
    print("not found")
