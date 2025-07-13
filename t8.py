def ThreeSum(list):
    list=sorted(list)
    result=[]
    for i in range(len(list)):
        if i>0 and nums[i]==nums[i-1]:
            continue

        left,right=i+1,len(list)-1
        while left<right:

            total=nums[i]+nums[left]+nums[right]
            if total==0:
                result.append([nums[i],nums[left],nums[right]])
            elif total<0:
                if nums[left]==nums[left+1]:
                    left+=1
                left+=1
            else:
                if nums[right]==nums[right-1]:
                    right-=1
                right-=1



            

            
