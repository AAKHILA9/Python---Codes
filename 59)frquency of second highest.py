nums=[1,2,2,3,3,3,4,4,4,4]
ans=""
high=0
h={}
maxx=max(nums)
for i in nums:
    if i not in h:
        h[i]=1
    else:
        h[i]+=1
for key,_ in h.items():
    if key>high and key<maxx:
        high=key
print(h[high])


nums=[1,2,2,3,3,3,4,4,4,4]
count={}
for i in nums:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
    maximum=0
    second_largest=0
    for key,value in count.items():
        if value>=maximum:
            second_largest=maximum
            maximum=value
print(second_largest)
            