str=input()
k=int(input())
freq={}
count=0
start=0
maxlength=0
for i in range(0,len(str)):
    if str[i] in freq:
        freq[str[i]]+=1
    else:
        freq[str[i]]=1
    if len(freq)==k:
        if i-start+1>maxlength:
            maxlength=i-start+1
    while len(freq)>k:
        freq[str[start]]-=1
        if freq[str[start]]==0:
            del freq[str[start]]
        start+=1

print(maxlength)


    

