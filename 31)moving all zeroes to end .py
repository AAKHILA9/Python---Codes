nums = [0, 1, 0, 3, 12]
result = []
for num in nums:
    if num != 0:
        result.append(num)
zeros = nums.count(0)
result += [0] * zeros
print(result)
    
    
    #OR
nums = [1,1, 0, 3, 12]  
n=len(nums)
i=0

for j in range(n):
    if nums[j]!=0:
        temp=nums[j]
        nums[j]=nums[i]
        nums[i]=temp
        i+=1
print(nums)

    