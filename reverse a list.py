nums=[1,2,8,4,5,6,7]
ans=nums[::-1]
print(ans)

#OR
nums=[1,2,8,4,5,6,7]
ans=[]
for i in range(len(nums)-1,-1,-1):
    ans.append(nums[i])
print(ans)

#OR
nums=[1,2,8,4,5,6,7]
print(nums)
n=len(nums)-1
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i]
    nums[n-i]=temp
print(nums)