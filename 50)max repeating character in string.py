s="oops"
dict={}
ans=0
for i in s:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
for key,value in dict.items():
    if value>ans:
        ans=value
        max_value=key
print(max_value,ans)