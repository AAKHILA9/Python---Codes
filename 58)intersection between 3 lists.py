nums1=[1,2,2,3,4]
nums2=[1,2,8,5]
nums3=[1,2,6,7]
ans=[]
for i in nums1:
    if i in nums2 and nums3:
        ans.append(i)
        nums1.remove(i)
        nums2.remove(i)
        nums3.remove(i)
print(ans)



nums1=set([1,2,2,3,4])
nums2=set([1,2,8,5])
nums3=set([1,2,6,7])
ans=[]
for i in nums1:
    if i in nums2 and nums3:
        ans.append(i)
print(ans)