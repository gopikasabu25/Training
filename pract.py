def p(l,k):
    for i in range(0,len(l)):
        left=i+1
        right=len(l)-1
        while left<right:
            sum = l[i]+l[left]+l[right]
            if sum==k:
                print("true")
                return
            elif sum<k:
                left=left+1
            else:
                right=right-1
    print("false")

l=list(map(int,input().split(",")))
k=int(input())
l.sort()
p(l,k)