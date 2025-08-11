n = "identify a bug"
ans = ""
n = n.split()
for i in range(len(n)):
    word = n[i]
    if len(word) == 1: 
        ans += word.upper() +" "
    else:
        ans += word[0].upper() + word[1:-1].lower() + word[-1].upper() +" "
print(ans.strip())

#or
str= "identify a bug"
n=len(str)
ans=""
for i in range(n):
    if i<n-1:
        if i==0 or str[i+1]==" " or str[i-1]==" ":
            st=str[i].upper()
            ans+=st
        else:
            ans+=str[i]
    else:
        st=str[i].upper()
        ans+=st
print(ans)