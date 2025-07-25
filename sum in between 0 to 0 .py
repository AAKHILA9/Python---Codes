nums=[0,1,0,3,0,2,2,0]
ans=[]
summ=0
for i in nums:
    if i!=0:
        summ+=i
    else:
        if summ>0:
            ans.append(summ)
        summ=0
print(ans)