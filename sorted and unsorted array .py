heights=[1,1,4,2,1,3]
expected=[1,1,1,2,3,4]
count=0
for i in range(len(heights)):
    if heights[i]!=expected[i]:
        count+=1
print(count)
            
        