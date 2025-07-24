nums=[2,3,1,2,3]
ans=[]
temp=nums.copy()
for i in temp:
    nums.remove(i)
    if i in nums and i not in ans:
        ans.append(i)
print(ans)