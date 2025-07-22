nums1=[1,2,2,5]
nums2=[2,2]
intersect=[]
for i in nums2:
    if i in nums1:
        intersect.append(i)
print("Intersection is:", intersect)
