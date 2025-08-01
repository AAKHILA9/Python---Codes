s="string"
i=3
prefix=s[:i][::-1]
suffix=s[i+1:]
ans=prefix+suffix
print(ans)

#OR
s="string"
new=""
for letter in s:
    if letter=="i":
        new=new[::-1]
    else:
        new+=letter
print(new)