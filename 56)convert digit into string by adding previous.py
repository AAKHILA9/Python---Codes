n = "a3b5c7"
ans = ""
previous=""
for i in n:
    if i.islower():
        ans += i
        previous=i
    else:
        digit=int(i)
        a = chr(ord(previous) + digit)
        ans += a
print(ans)



str = "a3b5c7"
ans = ""
serial=97
for i in range(len(str)):
    if str[i].isdigit():
        ascii=serial+int(str[i])
        ans+=chr(ascii)
        serial+=1
    else:
        ans+=str[i]
print(ans)
