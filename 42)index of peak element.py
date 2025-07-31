nums=[1,2,1,3,5,6,4]
ans=0
peak=nums[0]
for i in range(len(nums)):
    if nums[i]>peak:
        peak=nums[i]
        ans=i
print(ans)
