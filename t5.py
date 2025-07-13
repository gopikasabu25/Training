def groupAnagrams(str):
    anagram={}
    for i in str:
        key=tuple(sorted(i))
        if key in anagram:
            anagram[key].append(i)
        else:
            anagram[key]=[i]
        
    return list(anagram.values())
            
l=list(input("array").split())  
print(groupAnagrams(l))  