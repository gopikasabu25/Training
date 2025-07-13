List=["Thumb","IndexFinger","MiddleFinger","RingFinger","PinkyFinger"]

n=int(input("enter the number"))
if n%5==1:
    print(List[0])
elif n%5==2:
    print(List[1])
elif n%5==3:
    print(List[2])
elif n%5==4:
    print(List[3])
elif n%5==0:
    print(List[4])
