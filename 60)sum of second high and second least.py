nums=[1,8,3,9,11,5]
minimum=min(nums)
maxx=nums[0]
new=[]
for i in nums:
    if i!=minimum:
        new.append(i)
    if i>maxx:
        second_high=maxx
        maxx=i
second_least=min(new)
sum=second_high+second_least
print(sum)
        