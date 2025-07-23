n=int(input("enter a number:"))
sum=0
if n==0:
    print(1)
elif n<0:
    print("invalid number")
else:
    for i in range(1,n):
        if n%i==0:
            sum+=i
if sum==n:
    print("perfect number")
else:
     print("not perfect number")   