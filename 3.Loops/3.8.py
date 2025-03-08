#program to find Armstrong number or not
n=int(input())
s=0
t=0
t=n
while t>0:
    r=t%10
    s+=r**3
    t//=10
if n==s:
    print(f"{n} is an amstrong number")
else:
    print(f"{n} is not an amstrong number")
