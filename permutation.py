from collections import Counter
str=input()
d=Counter(str)
c=0
for count in d.values():
    if count%2 !=0:
        c+=1

if c<=1:
    print("true")
else:
    print("false")
