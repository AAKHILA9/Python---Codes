num=1234
strr=str(num)
words=("zero","one","two","three","four","five","six","seven","eight","nine")
ans=""
for i in strr:
    ans+=words[ord(i)-ord('0')]+" "
print(ans.strip())