import re
def isPalindrome(s):
    s=re.sub(r'[^A-Za-z0-9]','',s)
    s=s.lower()
    p=s[::-1]
    return p==s
        

s=input()
print(isPalindrome(s))
        