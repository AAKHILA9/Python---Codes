str="bu@gs:11"
ans=""
for i in str:
    if i.isalpha():
        ans+=i
print(ans)

#or
str="bu@gs:11"
ans=""
for i in str:
    val=ord(i)
    if (val>64 and val<91)or (val>96 and val<123):
        ans+=i
print(ans)   
