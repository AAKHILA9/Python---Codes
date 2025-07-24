n=8
a=0
b=1
if n>=0:
    print(a,b,end=" ")
n=n-2
if n>=2:
    for i in range(n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")
        
        
#OR
n=6
a=0
b=1
if n==1:
    print(a)
else:
    print("\n",a,b,end=" ")
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c,end=" ")