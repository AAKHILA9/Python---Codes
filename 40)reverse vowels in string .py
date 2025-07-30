s="IceCreAm"
vowels=["a","e","i","o","u","A","E","I","O","U"]
s=list(s)
low=0
high=len(s)-1
while low<high:
    if s[low] in vowels and  s[high] in vowels:
        s[low], s[high] = s[high], s[low]
        low+=1
        high-=1
    elif s[low] not in vowels:
            low+=1
    else:
        high-=1
ans="".join(s)
print(ans)