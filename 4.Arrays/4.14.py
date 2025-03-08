#method to find the second largest number in an array
n=int(input("Enter the number of elements: "))
arr=[]

for i in range(n):
    num=int(input())
    arr.append(num)

if n<2:
    print("Array should have at least two elements.")
else:
    largest=second_largest=float('-inf')

    for num in arr:
        if num>largest:
            second_largest=largest
            largest=num
        elif num>second_largest and num!=largest:
            second_largest = num

    if second_largest==float('-inf'):
        print("No second largest number found (all elements might be the same).")
    else:
        print("Second largest number:", second_largest)
