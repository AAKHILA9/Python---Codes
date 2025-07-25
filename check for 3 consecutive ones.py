nums=[1,2,3,4,7,9,11]
found=False
count=0
for i in nums:
    if i%2!=0 :
        count+=1
    if count==3:
        found=True
else:
    count=0
print(found)