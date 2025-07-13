n=int(input("enter the k"))
list=list(map(int,input("enter array").split()))
seen=set()
count=0
for i in list:
    if n+i in seen:
        count+=1
    if n-i in seen:
        count+=1
    seen.add(i)
print(count)


        
                