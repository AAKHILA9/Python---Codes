s="10111111111110111111110111111111011111111111101"
count=0
for i in s:
    if i=="1":
        count+=1
    else:
        print(chr(64+count),end="")
        count=0
if count>0:
    print(chr(64+count),end="")