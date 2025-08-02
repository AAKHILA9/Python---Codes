s="we are programmers"
dict={}
ans=[]
for i in s:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]+=1
for key,value in dict.items():
    if value==1:
        ans.append(key)
print(ans)