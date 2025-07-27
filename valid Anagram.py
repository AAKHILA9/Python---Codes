str1="rat"
str2="art"
str1=sorted(str1)
str2=sorted(str2)
n=len(str1)

if n!=len(str2):
    print("Not Anagram")
else:
    for i in range(n):
        if str1[i]!=str2[i]:
            print("Not Anagram")
    else:
        print("Anagram")
            
        