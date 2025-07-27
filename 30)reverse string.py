nums=['H','e','l','l','0']
i=0
j=len(nums)-1
while i<j:
    nums[i],nums[j]=nums[j],nums[i]
    i+=1
    j-=1
print(nums)

#OR
nums=['H','e','l','l','0']
n=len(nums)-1
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i]
    nums[n-i]=temp
print(nums)