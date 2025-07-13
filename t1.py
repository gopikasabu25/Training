def substring(str,k):
    left=0
    frq={}
    maxlength=0

    for right in range(len(str)):
        if str[right] in frq:
            frq[str[right]]+=1
        else:
            frq[str[right]]=1
        if len(frq)==k:
            maxlength=max(maxlength,right-left+1)
        if len(frq)>k:
            frq[s[left]]-=1
            if frq[s[left]]==0:
                del frq[s[left]]
            left=left+1
    return maxlength

s=input("enter string")
k=int(input("enter k unique"))
m=substring(s,k)
print(m)

    