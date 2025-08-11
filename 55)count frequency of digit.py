n=124562848586
h={}
for i in str(n):
    if i not in h:
        h[i]=1
    else:
        h[i]+=1
print(h)
        