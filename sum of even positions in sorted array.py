nums=[10,20,30,40,50,60,70]
n=len(nums)
ans=0
for i in range(n//2):
    temp=nums[i]
    nums[i]=nums[n-i-1]
    nums[n-i-1]=temp
print(nums)
for i in range(0,n):
    if i%2==0:
        ans+=nums[i]
print(ans)


#OR
nums=[10,20,30,40,50,60,70]
ans=nums[::-1]
sum=0
for i in range (len(ans)):
    if i%2==0:
        sum+=ans[i]
print(sum)

#OR
nums=[10,20,30,40,50,60,70]
nums.sort()
sum=0
for i in range (len(ans)):
    if i%2==0:
        sum+=ans[i]
print(sum)