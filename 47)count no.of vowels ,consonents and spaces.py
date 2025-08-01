s="I Love Myself"
vowels=0
consonents=0
spaces=0
for i in s:
    if i.lower() in "aeiou":
        vowels+=1
    elif i.isalpha():
        consonents+=1
    elif i==" ":
        spaces+=1
print("vowels:", vowels)
print("consonents:",consonents)
print("spaces:", spaces)