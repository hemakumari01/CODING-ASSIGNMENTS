#program to print largest number among three numbers
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(f"{a} is largest")
elif b>a and b>c:
    print(f"{b} is largest")
else:
    print(f"{c} is l;argest")
