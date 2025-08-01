s="Debugging"
ans={}
for i in s:
    if i not in ans:
        ans[i]=1
    else:
        ans[i]+=1
print(ans)