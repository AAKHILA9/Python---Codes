nums=[2,1,8,8,4,9,6,3]
nums.sort()
print(nums)

#OR
nums=[2,1,8,8,4,9,6,3]
n=len(nums)-1
for i in range(n-1):
    for j in range(n):
        if nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
print(nums)