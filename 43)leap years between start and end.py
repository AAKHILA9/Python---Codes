start=2000
end=2050
for i in range(start,end):
    if (i)%4==0 and (i)%100!=0 or (i)%400==0:
        print(i,end=" ")