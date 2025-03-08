#function to calculate the average value of an array of integers
n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
t=0
for num in a:
    t+=num
if n>0:
    avg=t/n
    print(avg)
    
