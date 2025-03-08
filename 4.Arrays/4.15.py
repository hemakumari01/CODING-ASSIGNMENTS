#method to find number of even number and odd numbers in an array
n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

even_count=0
odd_count=0

for num in arr:
    if num%2==0:
        even_count+=1
    else:
        odd_count+=1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
