s="[)"
stack=[]
mapping={")":"(","]":"[","}":"{"}
for char in s:
    if char in mapping.values():
        stack.append(char)
    elif char in mapping:
        if not stack or stack[-1]!=mapping[char]:
            print("False")
            break
        stack.pop()
else:
    print("True" if not stack else "False")
        
        
        