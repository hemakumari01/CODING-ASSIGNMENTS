#Program to check whether a number is EVEN or ODD using switch
n=int(input())
switch={
    0: f"{n} is even",
    1: f"{n} is odd"
    }
print(switch[n%2])
