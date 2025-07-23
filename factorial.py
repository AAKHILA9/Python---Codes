n=5
fact=1
if n>=0:
    if n==0:
        print(fact)
    else:
        for i in range(1,n+1):
            fact=fact*i
print(fact)


#Or
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)