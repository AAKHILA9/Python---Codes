s=43
sum=0
while s>0:
    rem=s%10
    sum=sum+rem
    s=s//10
print("sum is :",sum,end=" " )
for i in range(2,sum):
    if sum%i==0:
        print("not a prime number")
else:
    print(" prime number")
 