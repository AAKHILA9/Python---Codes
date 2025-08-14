str=" i love programming "
ans=""
for i in range(len(str)-1):
    if str[i].isalpha():
        ans+=str[i]
    elif str[i]==" " and str[i+1]!=" " and i+1<len(str) and len(ans)>0:
        ans+=str[i]
print(ans)
        