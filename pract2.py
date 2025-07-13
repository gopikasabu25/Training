str=input()
count=0
for i in str:
    if i=='{':
        count+=1
    elif i=='}':
            count-=1
    if count<0:
            break;
if count==0:
    print("Matching")
else:
    print("Not Matching")
    


