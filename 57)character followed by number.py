str="a3b2c4"
ans=""
prev=""
for i in str:
    if i.islower():
        prev=i
    else:
        for val in range(int(i)):
            ans+=prev
print(ans)
    
    



str="a3b2c4"
ans=""
for i in range(len(str)):
    if str[i].isdigit():
        multiple=int(str[i])
        st=str[i-1]*multiple
        ans+=st
print(ans)