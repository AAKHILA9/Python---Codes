    #FIND THE MAAX ELEMENT IN THE GIVEN LIST
List=[3,5,7,9,3,2]
maximum=0
for i in range(len(List)):
    if List[i] > maximum:
        maximum=List[i]
print(maximum) 

   #OR
List=[3,5,7,9,3,2]
ans=sorted(List)
maxi=ans[-1]
print(maxi)


   #0R
nums=[3,5,7,9,3,2]
ans=max(nums)
print(ans)