s="syncfusion"
n=len(s)
ans=""
count=0
for i in range(n):
    ans+=s[i]
    count+=1
    if count==4:
        print(ans)
        ans=""
        count=0
    