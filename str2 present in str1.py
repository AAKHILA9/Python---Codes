str1=""
str2="y"
if str1 in str2:
    print(str2[-1])
else:
    ans=str2 not in str1
    print(ans)



    #OR
str1=""
str2="y"
for i in str2:
    if i in str1:
        print(i)