start=150
end=212
ans=[]
for i in range (start,end+1):
    if str(i)==str(i)[::-1]:
        ans.append(i)
print(ans)

