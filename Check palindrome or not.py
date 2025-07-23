name="MALAYALAM"
ans="".join(reversed(name))
if ans==name:
    print("palindrome")
else:
    print("not palindrome")
    
    #OR
name="MALAYALAM"
if name==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")