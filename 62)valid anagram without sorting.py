text1="rat"
text2="tar"
if len(text1)!=len(text2):
    print("not anagram")
else:
    t1={char:text1.count(char) for char in text1}
    t2={char:text2.count(char)for char in text2}
    if t1==t2:
        print("anagaram")
    else:
        print("not anagram")