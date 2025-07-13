l=list(map(int,input().split(",")))
maxp=0
minprice=float('inf')
for i in l:
    if i<minprice:
        minprice=i
    if i-minprice>maxp:
        maxp=i-minprice

print(maxp)


