n=int(input("enter the number"))
l=list(map(int,input("enter array:").split()))
m=set(l)
for i in range(0,n+1):
    if i not in m:
        print(i)
