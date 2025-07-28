nums=[3,4,2,6,7,1,0]
min=nums[0]
for i in range(len(nums)):
    if nums[i]<min:
        min=nums[i]
        index=i
print("min element:",min , "index:",i)

