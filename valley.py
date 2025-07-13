
str=input()
count=0
valley=0
flag=0
for i in str:
    if i=='U':
        count+=1
    if i=='D':
        count-=1
    if count<0:
        flag=1
    if count>=0 and flag==1:
        flag=0
        valley+=1
    
    
print(valley)