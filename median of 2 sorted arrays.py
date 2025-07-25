nums1=[1,2]
nums2=[8,4]
nums=nums1+nums2
nums.sort()
n=len(nums)
if n%2==0:
    median=(nums[n//2-1]+nums[n//2])/2
else:
    median=nums[n//2]
print(median)