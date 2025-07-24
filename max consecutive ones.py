nums=[1,1,0,1,1,1,1,0]
count=0
sum=0
for i in nums:
    if i==1:
        count+=1
    else:
        sum=max(sum,count)
        count=0
print(sum)