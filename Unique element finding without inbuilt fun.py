nums=[1,8,1,2,3,2,4,5,4,5]
unique=[]
for i in nums:
    if i not in unique:
        unique.append(i)
print("unique elements are:",unique)


#OR 
nums=[1,8,1,2,3,2,4,5,4,5]
unique=set(nums)
print("unique elemts are:", tuple(unique))

#OR
unique=[]
for i in nums:
    if unique.count(i)==0:
        unique.append(i)
print("unique elemnta are:",unique)
