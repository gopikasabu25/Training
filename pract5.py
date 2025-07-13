def hanoi(n,s,d,i):
    if n==1:
        print("Move ring 1 from ",s,"to",d)
        return
    hanoi(n-1,s,i,d)
    
    print("Move ring",n,"from ",s,"to",d)
    
    hanoi(n-1,i,d,s)
          
s=A
d=B
i=C
n=int(input())
hanoi(n,s,d,i)